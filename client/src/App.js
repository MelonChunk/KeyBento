import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Header from './components/Header';
import TopContent from './pages/TopContent';
import ExplorePage from './pages/ExplorePage';
import LoginPage from './pages/LoginPage';
import UserPage from './pages/UserPage';

export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<TopContent />} />
          <Route path="/explore" element={<ExplorePage/>}/>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/user/:username" element={<UserPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
  </Container>
  )
}