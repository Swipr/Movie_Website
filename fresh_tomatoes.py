import os
import webbrowser

import media

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Swipr's favorite movies!</title>
    <link rel='shortcut icon' type='image/x-icon' href='favicon.ico' />
    
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">

        @font-face {
            font-family: Vlump;
            src: url('Vlump.ttf')
        }
        @font-face {
            font-family: Stingray;
            src: url('Stingray.otf')
        }

        html, body {
            background: #171717;
            font-family: 'Stingray';
            font-style: italic;
            font-weight: 50;
            padding-top: 50px;
            line-height:normal;
        }

        h2 {
            color: #56C7C7;
        }
        
        img {
            vertical-align: middle;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .navbar {
            background-color: #111111;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }

        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }

        #trailer-video-container {
            width: 100%;
            height: 100%;
        }

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
            background-color: gray;
        }

        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: black;
        }

        /* Hover effect on images */

        .hoverable {
            transition: box-shadow .3s;
            transition: all .2s ease-in-out;
            box-shadow: 0 0 11px rgba(33, 33, 33, .2);
            cursor: pointer;
        }

        .hoverable:hover {
            transform: scale(1.1);
        }

        /* Animated navbar text */

        section {
            width: 100vw;
            height: 79px;
            border-bottom: 1px solid rgb(86, 199, 199);
            position: relative;
            display: flex;
            flex-flow: row wrap;
            justify-content: center;
            align-items: center;
        }

        section .container {
            position: relative;
            display: flex;
            flex-flow: row wrap;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
        }

        section .text {
            color: #714F5A;
            font-family: 'Vlump';
            font-weight: 100;
            font-style: italic
            cursor: pointer;
            letter-spacing: 10px;
            text-transform: uppercase;
        }

        .ghost .text {
            font-size: 25px;
            background: linear-gradient(90deg, #333 0%, #eee 33%, #eee 66%, #333 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 300%;
            transition: 2s ease all;
            -webkit-animation: ghost 5s linear infinite;
            animation: ghost 5s linear infinite;
        }

        .ghost .text.hidden {
            opacity: 0;
            transition: 1s ease all;
        }

        @-webkit-keyframes ghost {
            0% {
                background-position: 0;
            }
            100% {
                background-position: 300%;
            }
        }

        @keyframes ghost {
            0% {
                background-position: 0;
            }
            100% {
                background-position: 300%;
            }
        }

        .ghost-hover .text {
            background: linear-gradient(90deg, #333 0%, #eee 33%, #eee 66%, #333 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 300%;
            background-position: -100%;
            transition: 2s ease all;
        }

        .ghost-hover .text:hover {
            background-position: 50%;
        }

        .ghost-hover .text.hidden {
            opacity: 0;
            background-size: 900%;
            transition: 1.5s ease all;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie_tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                'id': 'trailer-video',
                'type': 'text-html',
                'src': sourceUrl,
                'frameborder': 0,
                'allowFullScreen':'True' //Fullscreen button enabled

            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
            $('.movie-tile').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });
        console.clear();

        $(document).ready(function () {
            $('.text').removeClass('hidden');

            $('.show').on('click', function () {
                $(this).parent().find('.text').removeClass('hidden');
            });

            $('.hide').on('click', function () {
                $(this).parent().find('.text').addClass('hidden');
            });


            //parallax text section
            var txt = $('.parallax .text').text();
            console.log(txt);
            $('.parallax .text').text('');

            for (var i = 0; i < txt.length; i++) {
                var ltr = txt[i];
                var classes;
                var dec;
                var dist = Math.floor(Math.random() * 20);

                if (i % 2 != 0) {
                    classes = 'bottom';
                    dec = Math.floor(Math.random() * 20);
                }
                else {
                    classes = 'top';
                    dec = Math.floor(Math.random() * 20) * (-1);
                }

                var span = "<span class=" + classes + " style='top:" + dec + "px; font-size:" + (12 + (dist)) + "px' data-dist=" + dist + ">" + ltr + "<div class='ltr'>" + ltr + "</div></span>";
                $('.parallax .text').append(span);

                if (12 + (dist * 2) <= 30) {
                    $('.parallax .text span').last().css('filter', 'blur(1px)');
                }
            }

            $('.parallax .container').on('mousemove', function (event) {
                var x = (event.pageX / $(window).width() * 100) - 50;
                var y = ((event.pageY - $('.parallax').offset().top) / 650 * 100) - 50;
                $('.parallax .text span').each(function (i) {
                    var thisdist = $(this).attr('data-dist');
                    $(this).find('.ltr').css('transform', 'translate(' + (x / 10 * thisdist) + 'px, ' + (y / 10 * thisdist) + 'px)');
                });
            });


        });

    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
<!-- Trailer Video Modal -->
<div class="modal" id="trailer">
    <div class="modal-dialog">
        <div class="modal-content">
            <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
            </a>
            <div class="scale-media" id="trailer-video-container">
            </div>
        </div>
    </div>
</div>

    <!-- Main Page Content -->
<div class="container">
    <div class="navbar navbar-fixed-top" role="navigation">
        <section class="ghost">
            <div class="container">
                <div class="text hidden">Swipr's favorite movie trailers</div>
            </div>
        </section>
    </div>
</div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''

<div class="col-md-6 col-lg-4 movie-tile text-center">
        <div>
            <img src="{movie_poster}" alt="{movie_story}"
                 class="hoverable movie_tile" data-trailer-youtube-id="{movie_trailer}" data-toggle="modal"
                 data-target="#trailer" width="220" height="342">
        </div>
        <h2>{movie_title}</h2>
    </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=media.Movie.fetch_title(movie, movie.id),
            movie_story=media.Movie.fetch_story(movie, movie.id),
            movie_poster=media.Movie.fetch_poster(movie, movie.id),
            movie_trailer=media.Movie.fetch_trailer(movie, movie.id)
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', "w")

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
