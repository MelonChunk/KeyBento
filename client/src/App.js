import Container from 'react-bootstrap/Container';
import ApiProvider from './contexts/ApiProvider';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Header from './components/Header';
import Content from './pages/Content';
import ExplorePage from './pages/ExplorePage';
import LoginPage from './pages/LoginPage';
import UserPage from './pages/UserPage';
import RegistrationPage from './pages/RegistrationPage';
import FlashProvider from './contexts/FlashProvider';

export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <FlashProvider>
          <ApiProvider>
            <Header />
            <Routes>
              <Route path="/" element={<Content />} />
              <Route path="/explore" element={<ExplorePage/>}/>
              <Route path="/login" element={<LoginPage />} />
              <Route path="/user/:username" element={<UserPage />} />
              <Route path="/register" element={<RegistrationPage />} />
              <Route path="*" element={<Navigate to="/" />} />
            </Routes>
            </ApiProvider>
          </FlashProvider>
        </BrowserRouter>
  </Container>
  )
}
