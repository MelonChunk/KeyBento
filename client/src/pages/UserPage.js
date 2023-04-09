import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TimeAgo from '../components/TimeAgo';
import Body from '../components/Body';
import Stack from 'react-bootstrap/Stack';
import Image from 'react-bootstrap/Image';
import Spinner from 'react-bootstrap/Spinner';
import Destinations from '../components/Destinations'

import { useApi } from '../contexts/ApiProvider';

export default function UserPage() {
  const { username } = useParams();
  const [user, setUser] = useState();
  const api = useApi();

  useEffect(() => {
    (async () => {
      const response = await api.get('/user/' + username);
      setUser(response.ok ? response.body : null);
    })();
  }, [username, api]);


  return (
    <Body sidebar>
      {user === undefined ?
        <Spinner animation="border" />
      :
        <>
          {user === null ?
            <p>User not found.</p>
          :
            <Stack direction="horizontal" gap={4}>
              <Image src={user.avatar_url + '&s=128'} roundedCircle />
              <div>
                <h1>{user.username}</h1>
                {user.about_me && <h5>{user.about_me}</h5>}
                <p>
                  Member since: <TimeAgo isoDate={user.join_date} />
                  <br />
                  Last seen: <TimeAgo isoDate={user.last_seen} />
                </p>
              </div>
              <Stack>
              <p>Your properties</p>
              <Destinations content={user.username} add limit={3} />
              </Stack>
            </Stack>
          }
        </>
      }
    </Body>
  );
}
