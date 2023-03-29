import Stack from 'react-bootstrap/Stack';
import Container from 'react-bootstrap/Container';
import Body from '../components/Body';
import { useState } from 'react';
import Spinner from 'react-bootstrap/Spinner';

export default function TopContent(){
  const user = {
    id: 1,
    first_name: 'Melon',
    last_name: 'Chunk'
  }
  const [destinations, setDestinations] = useState()
  // const destinations = [{id:1, location:'London'}, {id:2, location:'New York'}, {id:3, location:'Berlin'}];

  return (<Body sidebar>
            <Stack>
              <Container>
                <p>Hello {user.first_name} {user.last_name}, good to see you back!</p>
              </Container>
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
                }
                </>
              }
                </Container>
             </Stack>
           </Body>
  );
}
