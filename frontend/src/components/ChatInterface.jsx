import React, { useState, useEffect } from "react";
import { Send, Bot, User, Plus, MessageSquare, Trash2 } from "lucide-react";
import api from "../services/api";

const ChatInterface = () => {

  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const [conversations, setConversations] = useState([]);
  const [currentConversation, setCurrentConversation] = useState(null);

  const [user] = useState({
    id: 1
  });


  // Load conversations
  useEffect(() => {
    loadConversations();
  }, []);



  const loadConversations = async () => {

    try {

      const response = await api.get("/conversations/");

      setConversations(response.data);


      if(response.data.length > 0){

        setCurrentConversation(response.data[0]);

        loadMessages(response.data[0].id);

      }

    } catch(error){

      console.error(
        "Loading conversations failed:",
        error
      );

    }

  };




  const loadMessages = async(conversationId)=>{

    try{

      const response = await api.get(
        `/messages/conversation/${conversationId}`
      );


      setMessages(response.data);


    }catch(error){

      console.error(
        "Loading messages failed:",
        error
      );

    }

  };





  const createNewConversation = async()=>{


    try{


      const response = await api.post(
        "/conversations/",
        {
          title:`Cloud Security Chat ${conversations.length + 1}`,
          user_id:user.id
        }
      );


      setConversations([
        ...conversations,
        response.data
      ]);


      setCurrentConversation(response.data);

      setMessages([]);



    }catch(error){

      console.error(
        "Create conversation failed:",
        error
      );

    }

  };





  const clearConversation = ()=>{

    setMessages([]);

  };







  const sendMessage = async()=>{


    if(!input.trim())
      return;



    if(!currentConversation){

      alert(
        "Please create a new chat first"
      );

      return;

    }



    const userText = input;


    setMessages(prev=>[
      ...prev,
      {
        role:"user",
        content:userText
      }
    ]);



    setInput("");

    setLoading(true);




    try{


      const response = await api.post(
        "/ai/chat",
        {

          message:userText,

          conversation_id:
          currentConversation.id,

          user_id:user.id

        }
      );




      setMessages(prev=>[
        ...prev,
        {
          role:"assistant",
          content:
          response.data.response
        }
      ]);




    }catch(error){


      console.error(
        "AI Error:",
        error
      );


      setMessages(prev=>[
        ...prev,
        {
          role:"assistant",
          content:
          "❌ Unable to connect with AI"
        }
      ]);


    }



    finally{

      setLoading(false);

    }


  };





  const handleKeyPress=(e)=>{

    if(
      e.key==="Enter" &&
      !e.shiftKey
    ){

      e.preventDefault();

      sendMessage();

    }

  };







return (

<div className="flex gap-4 h-[600px]">


{/* Sidebar */}

<div className="w-64 bg-white/5 rounded-xl border border-white/10 p-4 flex flex-col">


<button

onClick={createNewConversation}

className="mb-4 px-4 py-2 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg text-white font-semibold flex items-center justify-center gap-2"

>

<Plus size={18}/>

New Chat

</button>





<div className="flex-1 overflow-y-auto space-y-2">


{
conversations.map(conv=>(


<button

key={conv.id}

onClick={()=>{

setCurrentConversation(conv);

loadMessages(conv.id);

}}

className={`w-full text-left px-3 py-2 rounded-lg flex gap-2 ${
currentConversation?.id===conv.id
?
"bg-purple-500/20 text-white"
:
"text-gray-400 hover:bg-white/5"
}`}

>


<MessageSquare size={16}/>


<span className="truncate">

{conv.title}

</span>


</button>


))

}


</div>





<button

onClick={clearConversation}

className="mt-4 px-4 py-2 bg-red-500/10 text-red-400 rounded-lg flex items-center justify-center gap-2"

>

<Trash2 size={16}/>

Clear Chat

</button>



</div>








{/* Chat Area */}


<div className="flex-1 flex flex-col bg-white/5 rounded-xl border border-white/10">



<div className="p-4 border-b border-white/10">


<h3 className="text-white font-semibold">

{
currentConversation
?
currentConversation.title
:
"Select Chat"
}

</h3>


</div>







<div className="flex-1 overflow-y-auto p-4 space-y-4">


{
messages.length===0 &&

<div className="text-center text-gray-400 mt-20">

<Bot className="mx-auto mb-4 text-purple-400"/>

<p>
Start conversation with SCORE AI
</p>

</div>

}






{
messages.map((msg,index)=>(


<div

key={index}

className={`flex gap-3 ${
msg.role==="user"
?
"justify-end"
:
""
}`}

>


{
msg.role==="assistant" &&

<div className="bg-purple-500 rounded-full p-2">

<Bot size={18}/>

</div>

}




<div

className={`max-w-[70%] p-3 rounded-lg whitespace-pre-wrap ${
msg.role==="user"
?
"bg-purple-600 text-white"
:
"bg-white/10 text-white"
}`}

>

{msg.content}

</div>





{
msg.role==="user" &&

<div className="bg-blue-500 rounded-full p-2">

<User size={18}/>

</div>

}



</div>


))

}







{
loading &&

<div className="text-gray-300">

SCORE AI is thinking...

</div>

}



</div>







<div className="p-4 border-t border-white/10">


<div className="flex gap-2">


<textarea

value={input}

onChange={
e=>setInput(e.target.value)
}

onKeyDown={handleKeyPress}

placeholder="Ask SCORE AI..."

className="flex-1 bg-white/5 border border-white/10 rounded-lg p-3 text-white"

/>




<button

onClick={sendMessage}

disabled={loading}

className="px-6 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg text-white"

>

<Send size={20}/>

</button>



</div>


</div>



</div>





</div>

);

};



export default ChatInterface;