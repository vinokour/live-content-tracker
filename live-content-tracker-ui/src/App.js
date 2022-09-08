import React, { useEffect, useState } from "react";
import axios from 'axios';
import Tweet from './Tweet';
import './App.css';


function App() {
  const [tweets, setTweets] = useState([]);


  const [csvData, setCsvData] = useState([['Date','Accout','Description','Caption', 'Tweet URL','Type','Likes','Comments','Quote Tweets','Retweets','Views']]);
  
  useEffect(() => {
     axios.get('http://127.0.0.1:5000/tweets/2022-07-26').then(({ data: tweetsResponse }) => {
      setTweets(tweetsResponse);
      console.log(tweetsResponse);
      
    
    
      
   });
  }, []);

  //  TODO: use above code to actually send request instead of using dummy data from ./tweetsResponse.json
  //  using setTimeout to delay the request half a second to mimic how this will actually work when
 


  return (
    <div className="App">
      <ul className="tweets">
        {tweets.map((tweet) => (
           
          <Tweet key={tweet.tweets} tweet={tweet} csvData={csvData} onYesClicked={() => {
    
            setCsvData([
            ...csvData,
            
            [tweet.created_at,tweet.username,tweet.description,tweet.text, 'https://twitter.com/twitter/status/' + tweet.id,tweet.attachments[0].type,tweet.public_metrics.like_count,tweet.public_metrics.comment_count,tweet.public_metrics.quote_count,tweet.public_metrics.retweet_count,tweet.attachements.public_metrics.view_count]
          ])}}/>
        ))}
      </ul>
    </div>
  );
}
export default App;
