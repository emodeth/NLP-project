"use client";
import { useContext, createContext } from "react";
import axios from "axios";

const AppContext = createContext();

async function postPDF(data) {
  let formData = new FormData();
  formData.append("file", data);

  axios.post("http://localhost:5000/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
}

function AppProvider({ children }) {
  return (
    <AppContext.Provider value={{ postPDF }}>{children}</AppContext.Provider>
  );
}

function useApp() {
  const context = useContext(AppContext);
  if (!context) return;
  return context;
}

export { AppProvider, useApp };
