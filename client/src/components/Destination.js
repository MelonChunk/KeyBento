import Image from 'react-bootstrap/Image';
import Stack from 'react-bootstrap/Stack';
import Button from 'react-bootstrap/Button';
import { useApi } from '../contexts/ApiProvider';
import { useFlash } from '../contexts/FlashProvider';
import { useUser } from '../contexts/UserProvider';

export default function Destination({ destination, showOwner }) {
  const api = useApi();
  const flash = useFlash();
  const { user: loggedInUser } = useUser();

  const removeProperty = async () => {
    const response = await api.post('/remove_property', {
      id: destination.id
    });
    if (response.ok) {
      flash('Property removed', 'success');
    }
  };

  return (
    <>
      <Stack direction="horizontal" gap={3} className="Post">
        <li>
        {destination.type} in {destination.city}, {destination.country}
        {showOwner ? <> by {destination.owner.username} </> : null}
        <br/>
        {destination.description}
        {loggedInUser.id === destination.owner.id ? <Button variant="outline-secondary" onClick={removeProperty}> Remove listing </Button> : null}
        </li>
        <Image src={null} alt={destination.location} roundedCircle />
      </Stack >
    </>
  );
}
