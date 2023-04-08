import Container from 'react-bootstrap/Container';
import TimeAgo from './TimeAgo';
import { useUser } from '../contexts/UserProvider';

export default function Greeting(){

  const { user } = useUser();

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
