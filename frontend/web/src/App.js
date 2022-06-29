import logo from './logo.png';
import './App.css';
import { Capita, DailyGraph } from './pages';
import { Routes, Route } from "react-router-dom";
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Capita />} />
        <Route exact path="/dashboard" element={<Dashboard />} />
      </Routes>
    </div>
  );
}

export default App;
