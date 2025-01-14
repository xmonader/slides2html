"""
Reveal.js templates to be used in rendering websites.



"""

BASIC_TEMPLATE = """
<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>Basic Website</title>


		<link rel="stylesheet" href="https://unpkg.com/reveal.js@4.1.3/dist/reveal.css" />
		<script src="https://unpkg.com/reveal.js@4.1.3/dist/reveal.js"></script>
		<!-- Theme used for syntax highlighting of code -->
		
        <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.1.3/dist/theme/black.css"/>
  <!-- Printing and PDF exports -->
  
  

</head>

<body>
    <div class="reveal">
        <div class="slides">
            {% for slideinfo in slidesinfos %}
            <section>
                <div class="slide-image">
                    {{slideinfo['slide_image']}}
                </div>
                {% if slideinfo['slide_meta'] | length > 0 %}
                    <aside class="notes">
                        {% for el in slideinfo['slide_meta'] %}
                        <a class="slide-meta-item" href={{el}} target="_blank">{{el}},</a>
                        {% endfor %}
                    </aside>
                {% endif %}
            </section>
            {% endfor %}
        </div>
    </div>


    <script>
        // More info about config & dependencies:
        // - https://github.com/hakimel/reveal.js#configuration
        // - https://github.com/hakimel/reveal.js#dependencies
        Reveal.initialize({

            showNotes: true
        });
    </script>
</body>

</html>
"""
