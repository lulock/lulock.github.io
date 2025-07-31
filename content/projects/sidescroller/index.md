---
title: "Simple HTML side-scroller"
showDate: false
summary: "Sidescroller co-developed with ChatGPT for Ethics of Game AI workshop at European Conference on AI."
cascade:
    showAuthor: false
---
{{< rawhtml >}}
<!DOCTYPE html>
<html lang="en">
      <head>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.8.0/p5.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.8.0/addons/p5.sound.min.js"></script>
            <script src="sketch.js"></script>
            <link rel="stylesheet" type="text/css" href="style.css">
            <meta charset="utf-8" />
          </head>
      <body>
        <script>
  window.addEventListener("keydown", function (e) {
    // Prevent spacebar scrolling if focus is not in an input/textarea
    if (
      (e.code === "Space" || e.key === " " || e.keyCode === 32)
    ) {
      e.preventDefault();
    }
  });
</script>
        <div class="col-lg-6" id="welcome">
            This is a small project I worked on while developing the Workshop on Ethics in Games AI at the European Conference on AI conference 2023.<br><br> 

            The landing page of the workshop featured this simple side-scroller which I co-created with ChatGPT as an example usecase of AI in game development.<br><br>

            The game is written in JavaScript using the p5.js library. I've played around with p5.js before; you can check out some of those sketches <a href="">here</a>.
        </div>
        <div id="sketch-container" class="col-lg-6" autofocus
            title="This game was co-created with chatGPT.">
            <!-- <div id = "sketch-container" class="image-container" > -->
            <!-- <img alt="alternative" class="img-fluid" src="./EGAI workshop_files/2825132-637490944552534550-16x9-1.jpg"> -->
            <div id="" class="col-sm-12">
                <!-- <div id = "sketch-container" class="image-container" > -->
                <!-- <img alt="alternative" class="img-fluid" src="./EGAI workshop_files/2825132-637490944552534550-16x9-1.jpg"> -->
                <p class="p-large"></p>
            </div> <!-- end of image-container -->
        </div> <!-- end of image-container -->

          </body>
</html>


{{</ rawhtml >}}

### Check out the full website repo below! :point_down:

{{< github repo="egai-workshop/egai-workshop.github.io" showThumbnail=true >}}

