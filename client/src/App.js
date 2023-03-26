import Container from 'react-bootstrap/Container';
import Header from './components/Header';
import TopContent from './components/TopContent';
import Body from './components/Body';

export default function App() {
  return (
    <Container fluid className="App">
    <Header />
    <Body sidebar>
      <TopContent />
    </Body>
  </Container>
  )
}
