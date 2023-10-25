// // Function to make an API request to chatGPT
// function getChatGPTResponse() {
//     const apiKey = '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'; // Replace with your OpenAI API key
//     const apiUrl = 'https://api.openai.com/v1/engines/davinci-codex/completions';

//     const userInput = document.getElementById('userInput').value;

//     const requestData = {
//         prompt: userInput,
//         max_tokens: 5, // Adjust this value as needed
//     };

//     fetch(apiUrl, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `Bearer ${apiKey}`
//         },
//         body: JSON.stringify(requestData)
//     })
//     .then(response => response.json())
//     .then(data => {
//         const chatGPTResponse = data.choices[0].text;
//         document.getElementById('chatGPTResponse').innerHTML = `<p>ChatGPT Response:</p><p>${chatGPTResponse}</p>`;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         document.getElementById('chatGPTResponse').innerHTML = '<p>Error occurred while fetching the response.</p>';
//     });
// }

// document.getElementById('getResponseButton').addEventListener('click', getChatGPTResponse);
import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const response = await openai.chat.completions.create({
  model: "gpt-3.5-turbo",
  messages: [
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature: 1,
  max_tokens: 256,
  top_p: 1,
  frequency_penalty: 0,
  presence_penalty: 0,
});