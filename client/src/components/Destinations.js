import { useState, useEffect } from 'react';
import Spinner from 'react-bootstrap/Spinner';
import Container from 'react-bootstrap/Container';
import Destination from './Destination';
import { useApi } from '../contexts/ApiProvider';

export default function Destinations(){

  const [destinations, setDestinations] = useState()
  const api = useApi();

  useEffect(() => {
    (async () => {
      const response = await api.get('/destinations');
      if (response.ok) {
        setDestinations(response.body);
      }
      else {
        setDestinations(null);
      }
    })();
  }, [api]);

  return (
      <Container>
        {destinations === undefined ?
            <Spinner animation="border"/>
        :
        <>
        <p>The following destinations are available: </p>
          {destinations.length === 0 ?
              <p> Unfortunately, no destinations are currently available </p>
            :
            <ul>{destinations.map(destination => <Destination key={destination.id} destination={destination}/>)}</ul>
          }
        </>
      }
        </Container>
    )

}
