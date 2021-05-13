# What is API ?

What is an API?link to this section
If you’ve heard the term API before, chances are it’s been used not to refer to APIs in general, but instead to a specific kind of API, the web API. A web API allows for information or functionality to be manipulated by other programs via the internet. For example, with Twitter’s web API, you can write a program in a language like Python or Javascript that can perform tasks such as favoriting tweets or collecting tweet metadata.

In programming more generally, the term API, short for Application Programming Interface, refers to a part of a computer program designed to be used or manipulated by another program, as opposed to an interface designed to be used or manipulated by a human. Computer programs frequently need to communicate amongst themselves or with the underlying operating system, and APIs are one way they do it. In this tutorial, however, we’ll be using the term API to refer specifically to web APIs.

## When to Create an APIlink to this section
In general, consider an API if:

Your data set is large, making download via FTP unwieldy or resource-intensive.
Your users will need to access your data in real time, such as for display on another website or as part of an application.
Your data changes or is updated frequently.
Your users only need access to a part of the data at any one time.
Your users will need to perform actions other than retrieve data, such as contributing, updating, or deleting data.
If you have data you wish to share with the world, an API is one way you can get it into the hands of others. However, APIs are not always the best way of sharing data with users. If the size of the data you are providing is relatively small, you can instead provide a “data dump” in the form of a downloadable JSON, XML, CSV, or SQLite file. Depending on your resources, this approach can be viable up to a download size of a few gigabytes.

Remember that you can provide both a data dump and an API, and individual users may find one or the other to better match their use case. Open Library, for example, provides both a data dump and an API, each of which serves different use cases for different users.


<ul>
  <li><strong>HTTP (Hypertext Transfer Protocol)</strong> is the primary means of communicating data on the web. HTTP implements a number of “methods,” which tell which direction data is moving and what should happen to it. The two most common are GET, which pulls data from a server, and POST, which pushes new data to a server.</li>
  <li><strong>URL (Uniform Resource Locator)</strong> - An address for a resource on the web, such as <code class="language-plaintext highlighter-rouge">https://programminghistorian.org/about</code>. A URL consists of a <strong>protocol</strong> (<code class="language-plaintext highlighter-rouge">http://</code>), domain (<code class="language-plaintext highlighter-rouge">programminghistorian.org</code>), and optional <strong>path</strong> (<code class="language-plaintext highlighter-rouge">/about</code>). A URL describes the location of a specific resource, such as a web page. When reading about APIs, you may see the terms <code class="language-plaintext highlighter-rouge">URL</code>, <code class="language-plaintext highlighter-rouge">request</code>, <code class="language-plaintext highlighter-rouge">URI</code>, or <code class="language-plaintext highlighter-rouge">endpoint</code> used to describe adjacent ideas. This tutorial will prefer the terms URL and request to avoid complication. You can follow a URL or make a GET request in your browser, so you won’t need any special software to make requests in this tutorial.</li>
  <li><strong>JSON (JavaScript Object Notation)</strong> is a text-based data storage format that is designed to be easy to read for both humans and machines. JSON is generally the most common format for returning data through an API, XML being the second most common.</li>
  <li><strong>REST (REpresentational State Transfer)</strong> is a philosophy that describes some best practices for implementing APIs. APIs designed with some or all of these principles in mind are called REST APIs. While the API outlined in this lesson uses some REST principles, there is a great deal of disagreement around this term. For this reason, I do not describe the example APIs here as REST APIs, but instead as web or HTTP APIs.</li>
</ul>
