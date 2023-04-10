import Body from '../components/Body';
import Destinations from '../components/Destinations'


export default function ExplorePage() {
  return (
    <Body sidebar>
      <Destinations content='explore' showOwner limit={5}/>
    </Body>
  );
}
