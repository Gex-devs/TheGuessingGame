import React, { useState } from "react";
import "./Header.scss";
import temp_img from "../../assets/__Idle.gif";
import temp_img_2 from "../../assets/playBtn.png";
import { useNavigate } from "react-router-dom";
import temp_img3 from "../../assets/flip_skel.gif"
//import temp_img_2 from '../../assets/flip_skel.gif';

//var ReactDOM = require('react-dom');
var GifPlayer = require("react-gif-player");

/*function set_name()
{
  
  //fetch(`http://127.0.0.1:8000/setname/ggs`).then(Response => console.log(Response.status))
}*/

const Header = () => {
  let navigate = useNavigate();
  const [message, setMessage] = useState("");

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const mothertucker = (event) => {
    console.log(message);
    if (message.length > 5) {
      alert("Too many characters");
    } else {
      fetch(`http://127.0.0.1:8000/setname/${message}`).then((Response) =>
        console.log(Response.status)
      );
      navigate("/charSel");
    }
  };

  return (
    <div className="header">
      <h2>GUESS TO LIVE</h2>
      <button className="sd">
        <img src={temp_img_2} alt="look" className="sound_ico"></img>
      </button>
      <input
        type="text"
        value={message}
        onChange={handleChange}
        id="playerName"
        className="input_prt"
        placeholder="Player"
        maxLength={10}
      ></input>
      <button className="btn" onClick={mothertucker}>
        <text className="TextStyle">PLAY</text>
      </button>
      <div className="players">
        <GifPlayer className="kni" gif={temp_img} still={temp_img} />
        <GifPlayer className="skel" gif={temp_img3} still={temp_img3} />
      </div>
    </div>
  );
};

export default Header;
