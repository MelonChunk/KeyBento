import { useState, useEffect } from 'react';
import Spinner from 'react-bootstrap/Spinner';
import Container from 'react-bootstrap/Container';
import Destination from './Destination';

export default function Destinations(){

  const [destinations, setDestinations] = useState()


  useEffect(() => {
  (async () => {
      const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;
      const response = await fetch(BASE_API_URL + '/api/destinations');
      if (response.ok) {
        const destinations = await response.json();
        setDestinations(destinations);
      }
      else {
        setDestinations(null);
      }
      })(); }, []);

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
