import { useState, useEffect } from "react";
import { Navbar } from "./components/Navbar";
import IntegrationTerminal from './components/IntegrationTerminal';
import "./App.css";

function App() {
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem("theme") || "light";
  });

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light"));
  };

  return (
    <div className="app-container">
      <Navbar theme={theme} toggleTheme={toggleTheme} />
      <div className="app-layout-wrapper">
        <IntegrationTerminal />
      </div>
    </div>
  );
}

export default App;