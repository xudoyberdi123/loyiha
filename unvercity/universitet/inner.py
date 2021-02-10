def saaloom():
    return """
        <!DOCTYPE html>
        <html lang="en">
    
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    background-color: #262626;
                }
    
                ul {
                    position: absolute;
                    color: #484848;
                    font-family: sans-serif;
                    top: 50%;
                    left: 50%;
                    display: flex;
                    transform: translate(-50%, -50%)
                }
    
                ul li {
                    position: relative;
                    letter-spacing: 15px;
                    font-size: 15vh;
                    margin: 0;
                    padding: 0;
                    list-style: none;
                    animation: animate 1s linear infinite;
                }
    
                @keyframes animate {
    
                    0% {
                        color: #484848;
                        text-shadow: none;
                    }
    
                    0% {
                        color: #484848;
                        text-shadow: none;
                    }
    
                    0% {
                        color: rgb(17, 160, 255);
                        text-shadow: 0 0 7px rgb(17, 160, 255), 0 0 50px rgb(17, 160, 255);
                    }
    
                }
    
                ul li:nth-child(1) {
                    animation-delay: 0.2s;
                }
    
                ul li:nth-child(2) {
                    animation-delay: 0.4s;
                }
    
                ul li:nth-child(3) {
                    animation-delay: 0.6s;
                }
    
                ul li:nth-child(4) {
                    animation-delay: 0.8s;
                }
    
                ul li:nth-child(5) {
                    animation-delay: 1s;
                }
            </style>
        </head>
    
        <body>
            <ul>
                <li>S</li>
                <li>A</li>
                <li>L</li>
                <li>O</li>
                <li>M</li>
            </ul>
        </body>
    
        </html>
            """