import Stack from 'react-bootstrap/Stack';
import Body from '../components/Body';
import Destinations from '../components/Destinations'
import Greeting from '../components/Greeting'

export default function Content(){

  return (<Body sidebar>
            <Stack>
              <Greeting />
              <Destinations limit={10}/>
             </Stack>
           </Body>
  );
}
