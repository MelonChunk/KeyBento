import Stack from 'react-bootstrap/Stack';
import Container from 'react-bootstrap/Container';
import Body from '../components/Body';
import { useState, useEffect } from 'react';
import Spinner from 'react-bootstrap/Spinner';

export default function TopContent(){

  const [user, setUser] = useState()
  const [destinations, setDestinations] = useState()
  const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;

  useEffect(() => {
  (async () => {
      const response = await fetch(BASE_API_URL + '/api/destinations');
      if (response.ok) {
        const destinations = await response.json();
        setDestinations(destinations);
      }
      else {
        setDestinations(null);
      }
      })(); }, []);

  useEffect(() => {
  (async () => {
      const response = await fetch(BASE_API_URL + '/user/1');
      if (response.ok) {
        const user_data = await response.json();
        setUser(user_data);
      }
      else {
        setUser(null);
      }
      })(); }, []);


  return (<Body sidebar>
            <Stack>
              {user ?
                <Container>
                <p>Hello {user.first_name} {user.last_name}, good to see you back!</p>
              </Container>
                :
              <Container>
              <p> No user set</p>
            </Container>
            }
              <Container>
                {destinations === undefined ?
                    <Spinner animation="border"/>
                :
                <>
                <p>The following destinations are available: </p>
                  {destinations.length === 0 ?
                      <p> Unfortunately, no destinations are currently available </p>
                    :
                    <ul>
                      {destinations.map(x => {return (
                          <p key={x.id}>
                          <li>{x.location}</li>
                          </p>
                        )})}
                    </ul>
                  }
                </>
              }
                </Container>
             </Stack>
           </Body>
  );
}
