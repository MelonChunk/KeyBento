import Stack from 'react-bootstrap/Stack';
import Body from '../components/Body';
import Greeting from '../components/Greeting'

export default function Content(){

  return (<Body sidebar>
            <Stack>
              <Greeting />
             </Stack>
           </Body>
  );
}
