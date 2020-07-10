import React, {useState} from 'react';

const Form = (props) => {
  const [url, setUrl] = useState("");
  return (
    <form>
      <input type="text"
      placeholder="url" 
      value={url} 
      onChange={e => setUrl(e.target.value)} />
      <button>Show me the receipts!</button>
    </form>
  );
}

export default Form