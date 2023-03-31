import Container from 'react-bootstrap/Container';
import ApiProvider from './contexts/ApiProvider';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Header from './components/Header';
import Content from './pages/Content';
import ExplorePage from './pages/ExplorePage';
import LoginPage from './pages/LoginPage';
import UserPage from './pages/UserPage';

export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <ApiProvider>
          <Header />
          <Routes>
            <Route path="/" element={<Content />} />
            <Route path="/explore" element={<ExplorePage/>}/>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/user/:username" element={<UserPage />} />
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
          </ApiProvider>
        </BrowserRouter>
  </Container>
  )
}
