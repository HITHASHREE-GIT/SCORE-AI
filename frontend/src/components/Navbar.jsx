import React from "react";

function Navbar() {
  return (
    <nav className="navbar">
      <h2>SCORE</h2>

      <div>
        <a href="#features">Features</a>
        <a href="#about">About</a>
        <button>Login</button>
      </div>
    </nav>
  );
}

export default Navbar;