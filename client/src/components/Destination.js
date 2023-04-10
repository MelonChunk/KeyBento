import Image from 'react-bootstrap/Image';
import Stack from 'react-bootstrap/Stack';

export default function Destination({ destination, showOwner }) {
  return (
    <>
      <Stack direction="horizontal" gap={3} className="Post">
        <li>
        {destination.type} in {destination.city}, {destination.country}
        <>
        {showOwner ? <> by {destination.owner.username} </> : null}
        </>
        <br/>
        {destination.description}
        </li>
        <Image src={null} alt={destination.location} roundedCircle />
      </Stack >
    </>
  );
}
