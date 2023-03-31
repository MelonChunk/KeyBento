import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import { useApi } from '../contexts/ApiProvider';

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
        </Container>
      :
        <Container>
        <p> No user set</p>
        </Container>
  }
    </>
)
}
