import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import { NavLink } from 'react-router-dom';
import { useUser } from '../contexts/UserProvider';

export default function Sidebar() {
  const { user, logout } = useUser();

  return (
    <Navbar sticky="top" className="flex-column Sidebar">
      <Nav.Item>
        <Nav.Link as={NavLink} to="/" end>Main</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link as={NavLink} to="/explore">Explore</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link as={NavLink} to={'/user/' + user.username}>Profile</Nav.Link>
      </Nav.Item>
      <Nav.Item onClick={logout}>
        <Nav.Link as={NavLink} to={'/login'}> Logout </Nav.Link>
      </Nav.Item>
    </Navbar>
  );
}
