import { useEffect, useState } from "react";
import "./Navbar.css";

export function Navbar({ theme, toggleTheme }) {
  const [stats, setStats] = useState({ stars: 0, forks: 0 });

  useEffect(() => {
    // Fetch live GitHub stats for your repo
    fetch("https://api.github.com/repos/iamazhaar/SAINT-1961")
      .then((res) => res.json())
      .then((data) => {
        if (!data.message) { // Ignore if API rate limit exceeded
          setStats({ stars: data.stargazers_count, forks: data.forks_count });
        }
      })
      .catch((err) => console.error("Failed to fetch GitHub stats", err));
  }, []);

  return (
    <nav className="navbar">
      <div className="nav-left">
        <span className="nav-logo">SAINT-1961</span>
      </div>

      <div className="nav-right">
        {/* Theme Toggle Button */}
        <button onClick={toggleTheme} className="icon-btn" aria-label="Toggle theme">
          {theme === "light" ? (
             <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
          ) : (
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
          )}
        </button>

        {/* GitHub Link & Stats */}
        <a 
          href="https://github.com/iamazhaar/SAINT-1961" 
          target="_blank" 
          rel="noreferrer" 
          className="github-link"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          <div className="github-stats">
            <span className="repo-name">iamazhaar/SAINT-1961</span>
            <div className="stats-numbers">
              <span>★ {stats.stars}</span>
              <span>⑂ {stats.forks}</span>
            </div>
          </div>
        </a>
      </div>
    </nav>
  );
}