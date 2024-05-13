"use client";
import { useContext, createContext } from "react";

const AppContext = createContext();

async function postPDF(data) {
  try {
    const response = await fetch("https://example.com/profile", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();
    console.log("Success:", result);
  } catch (error) {
    console.error("Error:", error);
  }
}
function AppProvider({ children }) {
  return (
    <AppContext.Provider value={{ postPDF }}>{children}</AppContext.Provider>
  );
}

function useApp() {
  const context = useContext(AppContext);
  if (!context) return;
  return AppContext;
}

export { AppProvider, useApp };
