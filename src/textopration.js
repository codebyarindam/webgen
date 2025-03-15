import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const TextOperation = () => {
  const { moduleName } = useParams();
  const [moduleData, setModuleData] = useState(null);

  useEffect(() => {
    // Fetch data or handle logic related to moduleName here
    console.log("Selected module:", moduleName);
    // Example: setModuleData(fetchModuleData(moduleName));
  }, [moduleName]);

  return (
    <div>
      <h2>Modify {moduleName}</h2>
      {/* Render module data or modify logic here */}
      <p>Modify module: {moduleName}</p>
    </div>
  );
};

export default TextOperation;
