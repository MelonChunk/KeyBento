import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TimeAgo from '../components/TimeAgo';
import Body from '../components/Body';
import Stack from 'react-bootstrap/Stack';
import Image from 'react-bootstrap/Image';
import Spinner from 'react-bootstrap/Spinner';
import Destinations from '../components/Destinations'
import Calendar from '../components/Calendar'
import { useUser } from '../contexts/UserProvider';
import { useApi } from '../contexts/ApiProvider';

export default function UserPage() {
  const { username } = useParams();
  const [profileUser, setProfileUser] = useState();
  const { user: loggedInUser } = useUser();
  const api = useApi();

  useEffect(() => {
    (async () => {
      const response = await api.get('/user/' + username);
      setProfileUser(response.ok ? response.body : null);

    })();
  }, [username, api, loggedInUser]);



  return (
    <Body sidebar>
      {profileUser === undefined ?
        <Spinner animation="border" />
      :
        <>
          {profileUser === null ?
            <p>User not found.</p>
          :
            <Stack direction="horizontal" gap={4}>
              <Stack direction="vertical">
              <Image src={profileUser.avatar_url + '&s=128'} roundedCircle />
              <div>
                <h1>{profileUser.username}</h1>
                {profileUser.about_me && <h5>{profileUser.about_me}</h5>}
                <p>
                  Member since: <TimeAgo isoDate={profileUser.join_date} />
                  <br />
                  Last seen: <TimeAgo isoDate={profileUser.last_seen} />
                </p>
              </div>
              <Calendar/>
              </Stack>
              <Stack>
              {profileUser.username === loggedInUser.username ? <p>Your properties</p> : <p>{username}'s propertie(s)</p>}
              <Destinations content={username} add={profileUser.username === loggedInUser.username} limit={3} />
              </Stack>
            </Stack>
          }
        </>
      }
    </Body>
  );
}
