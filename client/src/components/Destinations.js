import { useState, useEffect } from 'react';
import Spinner from 'react-bootstrap/Spinner';
import Container from 'react-bootstrap/Container';
import Destination from './Destination';
import { useApi } from '../contexts/ApiProvider';
import More from './More';

export default function Destinations({content, limit=3}){

  const [destinations, setDestinations] = useState()
  const [pagination, setPagination] = useState();
  const api = useApi();

  let url;
  switch (content) {
    case undefined:
      url = '/destinations';
      break;
    case 'explore':
      url = '/destinations';
      break
    default:
      url = `/userdestinations/${content}`;
      break;
  }


  useEffect(() => {
    (async () => {
      const response = await api.get(url, {limit:limit});
      if (response.ok) {
        setDestinations(response.body.destinations);
        setPagination(response.body.pagination);
      }
      else {
        setDestinations(null);
        setPagination(null);
      }
    })();
  }, [api, url]);


  const loadNextPage = async () => {
    const response = await api.get(url, {
      offset: pagination.offset + pagination.limit
    });
    if (response.ok) {
      setDestinations([...destinations, ...response.body.destinations]);
      setPagination(response.body.pagination);
    }
  };

  return (
      <Container>
        {destinations === undefined ?
            <Spinner animation="border"/>
        :
        <>
          {destinations.length === 0 ?
              <p> Unfortunately, no more destinations are currently available </p>
            :
            <ul>{destinations.map(destination => <Destination key={destination.id} destination={destination}/>)}</ul>
          }
          <More pagination={pagination} loadNextPage={loadNextPage} />
        </>
      }
        </Container>
    )

}
