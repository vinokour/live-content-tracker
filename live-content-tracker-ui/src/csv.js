import React, { useEffect, useState } from "react";
import CSVLink, { CSVDownload } from 'react-csv';

const headers=[
    { label: 'id', key: 'tweet.id' },
    { label: 'text', key: 'tweet.text' },
    { label: 'imageUrls', key: 'tweet.imageUrls' }
    
]
function csv({ tweet }) {
    return (
        <CSVDownload
        data={tweet} 
        headers={headers}
        filename="tweets.csv"
        target="_blank"
        >
            Download Me!
        </CSVDownload>
        
   )
};
export default csv;