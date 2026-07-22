import React, { useState } from "react";
import api from "../services/api";
import { useAuth } from "../context/AuthContext";

function Dashboard() {
  const { user, logout } = useAuth();

  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [conversationId, setConversationId] = useState(null);
  const [loading, setLoading] = useState(false);


  // Create conversation
  const createConversation = async () => {
    try {
      const response = await api.post("/conversations/", {
        title: "Cloud Security AI Chat",
        user_id: user?.id || 1,
      });

      setConversationId(response.data.id);

      return response.data.id;

    } catch (error) {
      console.error("Conversation Error:", error);
    }
  };


  // Send message to AI
  const sendMessage = async () => {

    if (!message.trim()) return;


    setLoading(true);

    const userMessage = {
      role: "user",
      content: message
    };


    setChat((prev) => [
      ...prev,
      userMessage
    ]);


    try {

      let id = conversationId;


      if (!id) {
        id = await createConversation();
      }


      const response = await api.post("/ai/chat", {

        message: message,

        conversation_id: id,

        user_id: user?.id || 1

      });



      const aiMessage = {

        role: "assistant",

        content: response.data.response

      };


      setChat((prev)=>[
        ...prev,
        aiMessage
      ]);



    } catch(error){

      console.error(error);


      setChat((prev)=>[
        ...prev,
        {
          role:"assistant",
          content:"❌ Error connecting to AI"
        }
      ]);

    }


    setMessage("");

    setLoading(false);

  };



  return (

    <div className="min-h-screen bg-slate-950 text-white p-6">


      <div className="flex justify-between items-center mb-8">


        <div>

          <h1 className="text-3xl font-bold">
            SCORE AI Dashboard
          </h1>


          <p className="text-gray-400">
            Cloud Security AI Assistant
          </p>

        </div>



        <button

          onClick={logout}

          className="bg-red-600 px-4 py-2 rounded"

        >
          Logout
        </button>


      </div>





      <div className="max-w-4xl mx-auto">


        <div className="bg-slate-900 rounded-xl p-5 h-[500px] overflow-y-auto">


          {chat.length === 0 && (

            <p className="text-gray-400 text-center">

              Ask SCORE AI anything about cloud security...

            </p>

          )}



          {chat.map((item,index)=>(


            <div

              key={index}

              className={`mb-4 p-3 rounded-lg ${
                
                item.role==="user"

                ? "bg-blue-600 ml-auto"

                : "bg-slate-700"

              } max-w-[80%]`}

            >

              <b>

                {item.role==="user"
                  ?"You"
                  :"SCORE AI"}

              </b>


              <p className="mt-1 whitespace-pre-wrap">

                {item.content}

              </p>


            </div>


          ))}



        </div>






        <div className="flex gap-3 mt-5">


          <input

            value={message}

            onChange={(e)=>setMessage(e.target.value)}

            onKeyDown={(e)=>{

              if(e.key==="Enter")
                sendMessage();

            }}

            placeholder="Ask about cloud security..."

            className="flex-1 p-3 rounded bg-slate-800 text-white"

          />



          <button

            onClick={sendMessage}

            disabled={loading}

            className="bg-blue-600 px-6 rounded"

          >

            {loading ? "Thinking..." : "Send"}

          </button>


        </div>



      </div>


    </div>

  );

}


export default Dashboard;