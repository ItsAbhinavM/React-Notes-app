import "./App.css";
import { useState, useEffect } from "react";
import axios from "axios";

function CreateList({ id, onDelete, onSave, notes }) {
  const [noteText, setContent] = useState("");
  useEffect(() => {
    console.log("inside the box :", notes.id,notes.noteText);
  }, []);
  
  const [date, setDate] = useState("");
  const handleChange = (event) => {
    setContent(event.target.value);
  };

  const handleSave = () => {
    onSave(id, noteText);
  };
  const handleDelete=()=>{
    onDelete(id);
  }
  const handleDate = (event) => {
    onSave(event.target.value);
  };

  return (
    <div
      className="inputBox"
      style={{ display: "flex", justifyContent: "center" }}
    >
      <textarea
        className="inputval"
        placeholder="Type here"
        defaultValue={notes.noteText}
        onChange={handleChange}
        style={{ minHeight: "200px" }}
      ></textarea>
      <div
        style={{
          display: "flex",
          justifyContent: "initial",
          flexDirection: "column",
        }}
      >
        <button
          style={{
            fontSize: "12px",
            borderRadius: "30px",
            height: "50px",
            margin: "2px",
            padding: "13px",
            backgroundColor: "orange",
          }}
          className="DeleteNote"
          onClick={() => handleDelete(id)}
        >
          Delete note
        </button>
        <button
          style={{
            fontSize: "12px",
            borderRadius: "30px",
            height: "50px",
            margin: "2px",
            padding: "13px",
            backgroundColor: "orange",
          }}
          className="SaveNote"
          onClick={() => handleSave(id)}
        >
          Save note
        </button>
        <p>Due date : </p>
        <input
          type="date"
          className="Date"
          defaultValue={notes.date}
          onChange={handleChange}
          /*onSave={handleDate}*/
          style={{
            maxHeight: "30px",
            minHeight: "10px",
            borderRadius: "18px",
            padding: "13px",
            backgroundColor: "gray",
          }}
        ></input>
      </div>
    </div>
  );
}

const Blabla = ({ data }) => {
  
  console.log("Data is : ", data);
  return(
    <div>
      <h1 style={{color: 'white'}}>{data.noteText}</h1>
    </div>
  )
}

export default function Myapp() {
  const [inputBoxes, setInputBoxes] = useState([]);

  useEffect(() => {
    fetchNotes();
  }, []);

  useEffect(() => {
    console.log(inputBoxes);
  }, [inputBoxes]);

  const fetchNotes = async () => {
    try {
      const response = await axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/djangonotes/",
      });
      setInputBoxes(response.data);
    } catch (error) {
      console.error("Error fetching the notes: ", error);
    }
  };

  const saveNote = async (id, content) => {
    try {
      await axios.put(`http://127.0.0.1:8000/api/djangonotes/${id}/`, {
      noteText: content
      });
      fetchNotes();
    } catch (error) {
      console.error("Error updating note : ", error);
    }
  };

  const createNote = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/djangonotes/",
        { noteText: "Enter note" }
      );
      console.log("Note created successfully : ", response.data);
      fetchNotes();
    } catch (error) {
      console.error("Error creating note : ", error);
    }
  };

  const deleteNote = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/delete/${id}`);
      
    }
    catch (error) {
      console.error("Error deleting note : ", error);
    }
    await fetchNotes();
    };

    /*const deleteNote = async (id) => {
      try {
        const response = await axios.delete(`http://127.0.0.1:8000/api/delete/${id}`);
    
        if (response.status === 204) {
          // Filter the local state to remove the deleted note
          setInputBoxes((prevBoxes) => prevBoxes.filter((note) => note.id !== id));
    
          // Fetch the updated notes from the server
          await fetchNotes();
    
          console.log("Note deleted successfully");
        } else {
          console.error("Error deleting note:", response.statusText);
        }
      } catch (error) {
        console.error("Error deleting note:", error);
      }
    };*/

  return (
    <div>
      <h1 align="Center">My Notes</h1>
      <button onClick={createNote}>Create a new note</button>
      {inputBoxes.map((box) => (
        <CreateList
           id={box.id}
           onDelete={deleteNote}
           onSave={saveNote}
           notes={box} />
      ))}
    </div>
  );
}
