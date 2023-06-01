const fileInput = document.querySelector(".file-input"),
conversionOptions = document.querySelectorAll('input[name="unt"]'),
rotateOptions = document.querySelectorAll(".rotate button"),
previewImg = document.querySelector(".preview-img img"),
resetImgBtn = document.querySelector(".reset-image"),
chooseImgBtn = document.querySelector(".choose-img"),
saveImgBtn = document.querySelector(".save-img");

let rotate = 0, flipHorizontal = 1, flipVertical = 1;
let selection = "crop", units = "imp";
let x1 = -1, x2 = -1, y1 = -1, y2 = -1;
let saveCt = 0;
let rate = 0;
let unts = "feet";

const loadImage = () => {
    let file = fileInput.files[0];
    if(!file) return;
    previewImg.src = URL.createObjectURL(file);
    previewImg.addEventListener("load", () => {
        resetImgBtn.click();
        document.querySelector(".container");
    });
}

const resetImg = () => {
    rotate = 0; flipHorizontal = 1; flipVertical = 1;
    applyRotation();
}

const applyRotation = () => {
    previewImg.style.transform = `rotate(${rotate}deg) scale(${flipHorizontal}, ${flipVertical})`;
}

rotateOptions.forEach(option => {
    option.addEventListener("click", () => {
        if(option.id === "left") {
            rotate -= 90;
        } else if(option.id === "right") {
            rotate += 90;
        } else if(option.id === "horizontal") {
            flipHorizontal = flipHorizontal === 1 ? -1 : 1;
        } else {
            flipVertical = flipVertical === 1 ? -1 : 1;
        }
        applyRotation();
    });
});

conversionOptions.forEach(option => {
    option.addEventListener("click", () => {
        for (const radioButton of conversionOptions)
        {
            if (radioButton.checked)
            {
                units = radioButton.value;
                console.log(units);
                break;
            }
        }
    });
});

function editor(x, y) //Maybe need to fix rate
{
    if (x1 == -1 && y1 == -1)
    {
        x1 = x;
        y1 = y;
    }
    else
    {
        x2 = x;
        y2 = y;
        d = Math.sqrt(Math.pow(x2-x1,2) + Math.pow(y2-y1,2));
        console.log(d);
        if (units === "imp")
        {
            unts = "feet";
            ft = prompt("Enter the number of feet:");
            inch = prompt("Enter the number of inches:");
            rate = (ft + (inch/12))/d;
            console.log(rate);
            x1 = -1, x2 = -1, y1 = -1, y2 = -1;
        }
        else if (units === "mtc")
        {
            unts = "meter(s)";
            m = prompt("Enter the number of meters:");
            cm = prompt("Enter the number of centimeters:");
            rate = (m + (cm/100))/d;
            console.log(rate);
            x1 = -1, x2 = -1, y1 = -1, y2 = -1;
        }
    }
}


// Function to handle mouse click event on the image
function handleClick(event)
{
  // Get the pixel coordinates of the click event relative to the image
  const rect = previewImg.getBoundingClientRect();
  const scaleX = previewImg.naturalWidth / rect.width;
  const scaleY = previewImg.naturalHeight / rect.height;
  let x = Math.round((event.clientX - rect.left) * scaleX);
  let y = Math.round((event.clientY - rect.top) * scaleY);

  if (x < 0)
  {
    x = 0;
  }
  else if (y < 0)
  {
    y = 0;
  }

  // Return the coordinates
  console.log({x,y});
  editor(x,y);
}

function calcSQ()
{
    const { exec } = require('child_process');

    // Run Python script with a file argument
    let filePath = "(your path) image (" + saveCt + ").jpg"; //Replace with the path to the file (fix)
    const pythonScript = 'path/to/your/python_script.py'; // Replace with the actual path to your Python script (fix)

    exec(`python ${pythonScript} ${filePath}`, (error, stdout, stderr) => {
    if (error)
    {
        console.error(`Error: ${error.message}`);
        return;
    }
    if (stderr)
    {
        console.error(`Python script encountered an error: ${stderr}`);
        return;
    }
    console.log(`Python script output: ${stdout}`);
    realSQ = stdout*rate;
    alert(`The square footage is ${realSQ} ${unts}.`);
    });
}

// Attach the click event listener to the image
previewImg.addEventListener('click', handleClick);

const saveImage = () => {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    canvas.width = previewImg.naturalWidth;
    canvas.height = previewImg.naturalHeight;
    
    ctx.translate(canvas.width / 2, canvas.height / 2);
    if(rotate !== 0) {
        ctx.rotate(rotate * Math.PI / 180);
    }
    ctx.scale(flipHorizontal, flipVertical);
    ctx.drawImage(previewImg, -canvas.width / 2, -canvas.height / 2, canvas.width, canvas.height);
    
    const link = document.createElement("a");
    link.download = "image.jpg";
    link.href = canvas.toDataURL();
    link.click();
    calcSQ();
}

saveImgBtn.addEventListener("click", saveImage);
fileInput.addEventListener("change", loadImage);
resetImgBtn.addEventListener("click", resetImg);
chooseImgBtn.addEventListener("click", () => fileInput.click());