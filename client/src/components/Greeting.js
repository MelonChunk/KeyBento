import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import { useApi } from '../contexts/ApiProvider';
import TimeAgo from './TimeAgo';


export default function Greeting(){

  const [user, setUser] = useState()
  const api = useApi();

  useEffect(() => {
  (async () => {
      const response = await api.get('/user/1');
      if (response.ok) {
        setUser(response.body);
      }
      else {
        setUser(null);
      }
    })(); }, [api]);



  return (
    <>
    {user ?
        <Container>
        <p>Hello {user.first_name} {user.last_name}, good to see you back!</p>
        <p>You have been with us since { <TimeAgo isoDate={user.join_date} />}</p>
        </Container>
      :
        <Container>
        <p> No user set</p>
        </Container>
  }
    </>
)
}
