import React from "react";
import styled from 'styled-components';
import csv from './csv';
import {CSVLink} from 'react-csv';

const space = styled.div`
  width: 4px;
  height: auto;
  display: inline-block;
`;

const NoButton = styled.button`
background-color: red;
  color: white;
  padding: 10px 60px;
  bordder-radius: 5px;
  outline: 0;
  cursor: pointer;
  boxshadow: 0px 2px 5px lightgrey;
  transition: ease background-color 250ms;
  &:hover {
    background-color: #283593;
`;
const YesButton = styled.button`
  background-color: green;
  color: black;
  padding: 10px 60px;
  border-radius: 5px;
  outline: 0;
  cursor: pointer;
  boxshadow: 0px 2px 5px lightgrey;
  transition: ease background-color 250ms;
  &:hover {
    background-color: red;
`;
const Wrapper = styled.div`
  padding: 4em;
  background: lightblue;
`;
const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: Black;
`;
const VideoType = styled.h1`
  font-size: 1em;
  text-align: center;
  text-decoration: underline;
  color: Black;
  `;
  const Account = styled.h1`
  font-size: 1em;
  text-align: center;
  color: Black;
  '&:hover {
    color: red;

  }
  `;


//function that gets data from api and writes into csv file



//This should work w api so user knows that a tweet was a retweet and not a tweet
function checkRT(tweet) {
  if (tweet.retweeted_status) {
    return <li className="retweet">{tweet.retweeted_status.caption}</li>;
  }
}




function Tweet({ tweet,  onYesClicked, csvData }) {

  

  
  return (
    //displays a message at the top of the page

     
    <Wrapper className="color">
        <Title>
          <Account>
            {"@"}{tweet.username}





          </Account>
          {tweet.text}
          <VideoType>
            {tweet.attachments[0].type}
          </VideoType>


        </Title>


        {tweet.attachments.map((attachment) => (
          <img key={attachment.media_key} src={attachment.url || attachment.preview_image_url} height={250} width={250}
            onClick={() => {
              //embed link to tweet
              window.open('https://twitter.com/twitter/status/' + tweet.id, '_blank');
            } } />

        ))}

        <div className="buttons">
          <label for="Description">Description:</label>
          <input
            type="text"
            id="Description"
            value={tweet.description}
            onChange={(e) => {
              tweet.description = e.target.value;
            } } />
          <div class="space">
            <space />
          </div>



          <YesButton onClick={() => onYesClicked(tweet)}>
            Yes
          </YesButton>
        </div>

        <CSVLink data={csvData}>
          Download
        </CSVLink>



      </Wrapper>
    
      
  );
}

export default Tweet;
