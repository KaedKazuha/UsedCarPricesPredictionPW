import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-blue-600 p-4 text-white">
      <div className="container mx-auto flex justify-between">
        <h1 className="text-xl font-bold">Car Price Predictor</h1>
        <ul className="flex space-x-4">
          <li><a href="/" className="hover:underline">Home</a></li>
          <li><a href="/predict" className="hover:underline">Predict Price</a></li>
          <li><a href="/about" className="hover:underline">About</a></li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
