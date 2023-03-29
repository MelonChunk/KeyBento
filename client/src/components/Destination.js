import Image from 'react-bootstrap/Image';
import Stack from 'react-bootstrap/Stack';

export default function Destination({ destination }) {
  return (
    <>
      <Stack direction="horizontal" gap={3} className="Post">
        <li>{destination.location}</li>
        <Image src={null} alt={destination.location} roundedCircle />
      </Stack >
    </>
  );
}
