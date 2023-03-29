import { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';

export default function Greeting(){

  const [user, setUser] = useState()
  const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;


  useEffect(() => {
  (async () => {
      const response = await fetch(BASE_API_URL + '/user/1');
      if (response.ok) {
        const user_data = await response.json();
        setUser(user_data);
      }
      else {
        setUser(null);
      }
      })(); }, []);



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
