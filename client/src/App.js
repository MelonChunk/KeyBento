import Container from 'react-bootstrap/Container';
import ApiProvider from './contexts/ApiProvider';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Header from './components/Header';
import Content from './pages/Content';
import ExplorePage from './pages/ExplorePage';
import LoginPage from './pages/LoginPage';
import UserPage from './pages/UserPage';
import RegistrationPage from './pages/RegistrationPage';
import RegisterInterestPage from './pages/RegisterInterestPage';
import FlashProvider from './contexts/FlashProvider';
import UserProvider from './contexts/UserProvider';
import PrivateRoute from './components/PrivateRoute';
import PublicRoute from './components/PublicRoute';

export default function App() {
  return (
        <Container fluid className="App">
          <BrowserRouter>
            <FlashProvider>
              <ApiProvider>
                <UserProvider>
                    <Header />
                    <Routes>
                      <Route path="*" element={<PublicRoute><RegisterInterestPage /></PublicRoute>} />
                     </Routes>
                </UserProvider>
            </ApiProvider>
          </FlashProvider>
        </BrowserRouter>
      </Container>
  );
}


// export default function App() {
//   return (
//     <Container fluid className="App">
//       <BrowserRouter>
//         <FlashProvider>
//           <ApiProvider>
//             <UserProvider>
//                 <Header />
//                 <Routes>
//                 <Route path="/login" element={<PublicRoute><LoginPage /></PublicRoute>} />
//                 <Route path="/register" element={<PublicRoute><RegistrationPage /></PublicRoute>} />
//                 <Route path="/register_interest" element={<PublicRoute><RegisterInterestPage /></PublicRoute>} />
//                 <Route path="*" element={
//                   <PrivateRoute>
//                     <Routes>
//                       <Route path="/" element={<Content />} />
//                       <Route path="/explore" element={<ExplorePage/>}/>
//                       <Route path="/user/:username" element={<UserPage />} />
//                       <Route path="*" element={<Navigate to="/" />} />
//                     </Routes>
//                   </PrivateRoute>
//                 } />
//                 </Routes>
//             </UserProvider>
//         </ApiProvider>
//       </FlashProvider>
//     </BrowserRouter>
//   </Container>
//   )
// }
