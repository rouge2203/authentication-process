import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className=" h-screen flex items-center justify-center bg-slate-900">
      <div className="flex flex-col items-center justify-center">
        <h1 className="text-3xl font-bold text-cyan-500">
          Hello Vite + React!
        </h1>
        <p className="text-md font-bold text-cyan-600 italic ">
          using tailwind css
        </p>
      </div>
    </div>
  );
}

export default App;
