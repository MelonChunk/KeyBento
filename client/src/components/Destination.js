import { useState, useEffect, memo } from 'react';
import Image from 'react-bootstrap/Image';
import Stack from 'react-bootstrap/Stack';
import Button from 'react-bootstrap/Button';
import { NavLink } from 'react-router-dom';
import { useApi } from '../contexts/ApiProvider';
import { useFlash } from '../contexts/FlashProvider';
import { useUser } from '../contexts/UserProvider';

export default memo(function Destination({ destination, showOwner }) {
  const api = useApi();
  const flash = useFlash();
  const { user: loggedInUser } = useUser();
  const [isOwnerLoggedIn, setIsOwnerLoggedIn] = useState(false);

  useEffect(() => {
    (async () => {
      if (destination.owner.id === loggedInUser.id) {
        setIsOwnerLoggedIn(true);
      }
      else {
        setIsOwnerLoggedIn(false);
      }
    })();
  }, [destination, api, loggedInUser]);

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
        {destination.type} in {destination.city.toUpperCase()}, {destination.country.toUpperCase()}
        {showOwner ? <> by <NavLink to={'/user/' + destination.owner.username}>{destination.owner.username} </NavLink> </> : null}
        <br/>
        {destination.description}
        {isOwnerLoggedIn ? <><br/><Button variant="outline-secondary" onClick={removeProperty}> Remove listing </Button></> : null}
        </li>
        <Image src={null} alt={destination.location} roundedCircle />
      </Stack >
    </>
  );
});
