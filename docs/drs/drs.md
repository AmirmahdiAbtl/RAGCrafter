# Title of the project

## Design Requirement Specification Document

DIBRIS – Università di Genova. Scuola Politecnica, Corso di Ingegneria del Software 80154

<div align='left'> <b> Authors </b> <br> - SOBHAN BAZOUBANDI <br> - AMIRMAHDI ABOUTALEBI <br> - AMIRHOSSEIN YAGHOUBNEZHAD  </div>

### REVISION HISTORY

| Version | Data       | Author(s)                                                          | Notes |
| ------- | ---------- | ------------------------------------------------------------------ | ----- |
| 4.0     | 03/07/2025 | SOBHAN BAZOUBANDI, AMIRMAHDI ABOUTALEBI, AMIRHOSSEIN YAGHOUBNEZHAD | Add Object Diagram |
| 3.0     | 03/07/2025 | SOBHAN BAZOUBANDI, AMIRMAHDI ABOUTALEBI, AMIRHOSSEIN YAGHOUBNEZHAD | Add Dynamic Models |
| 2.0     | 02/19/2025 | SOBHAN BAZOUBANDI, AMIRMAHDI ABOUTALEBI, AMIRHOSSEIN YAGHOUBNEZHAD | Add Class Diagram & Update System Overview sections |
| 1.0     | 09/23/2024 | SOBHAN BAZOUBANDI, AMIRMAHDI ABOUTALEBI, AMIRHOSSEIN YAGHOUBNEZHAD |

## Table of Content

1. [Introduction](#intro)
   1. [Purpose and Scope](#purpose)
   2. [Definitions](#def)
   3. [Document Overview](#overview)
   4. [Bibliography](#biblio)
2. [Project Description](#description)
   1. [Project Introduction](#project-intro)
   2. [Technologies used](#tech)
   3. [Assumptions and Constraints](#constraints)
3. [System Overview](#system-overview)
   1. [System Architecture](#architecture)
   2. [System Interfaces](#interfaces)
   3. [System Data](#data)
      1. [System Inputs](#inputs)
      2. [System Outputs](#outputs)
4. [System Module 1](#sys-module-1)
   1. [Structural Diagrams](#sd)
      1. [Class Diagram](#cd)
         1. [Class Description](#cd-description)
      2. [Object Diagram](#od)
      3. [Dynamic Models](#dm)
5. [System Module 2](#sys-module-2)
   1. ...

## <a name="intro"></a> 1 Introduction

### <a name="purpose"></a> 1.1 Purpose and Scope

<details> 
<br/><br/>
<summary>The primary goal of this design is to create an AI Assistant that effectively leverages the capabilities of Large Language Models (LLMs) to enhance the study platform. By implementing a RAG architecture, the Assistant will be able to retrieve relevant information from a knowledge base and generate contextually appropriate responses. This will enable the Assistant to provide valuable support to users in various development tasks, such as writing guidelines, tutorials, and generating code examples.
 </summary>
    <p><b>Key Design Principles:</b><br/>
    <ul>
<li>User-Centric Design: The Assistant's design will prioritize the needs and preferences of users. It will provide a user-friendly interface and offer intuitive interactions.</li>
<li>Knowledge Base Integration: The Assistant will seamlessly integrate with a well-structured knowledge base containing relevant information, such as guidelines, API specifications, and existing documents.</li>
<li>RAG Architecture: The Assistant will employ a RAG architecture to ensure that responses are contextually relevant and accurate. This will involve retrieving information from the knowledge base based on user queries and generating responses using the LLM.</li>
<li>Scalability: The design will be scalable to accommodate future growth and changes in the project requirements.</li>
<li>Security and Privacy: The Assistant will adhere to strict security and privacy standards to protect user data.</li></ul></p>
</details>

### <a name="def"></a> 1.2 Definitions

<details> 
     <summary> Here are listed some definitions used during the project development
    </summary>

| Acronym | Definition                                                         |
| ------- | ------------------------------------------------------------------ |
| RAG     | Retrieval-Augmented Generation                                     |
| LLM     | Large Language Models                                              |
| RA      | Review Assistant                                                   |
| WA      | Writer Assistant                                                   |
| DA      | App Developer Assistant                                            |
| LLaMA   | Family of autoregressive large language models released by Meta AI |
| NLP     | Natural Language Processing                                        |
| FT      | Fine Tuning                                                        |
| RNN     | Recurrent Neural Networks                                          |
| GAI     | Generative Artificial Intelligence                                 |
| AI      | Artificial Intelligence                                            |
| OAS     | OpenAPI Specification                                              |
| UI      | User Interface                                                     |

</details>

### <a name="overview"></a> 1.3 Document Overview

<details> 
    <summary> This document outlines the system design, including architecture, interfaces, data flow, and requirements.
    </summary>
    <p>This document is structured to provide a comprehensive understanding of the RAG-based AI Assistant for the internal development platform. It is divided into key sections as follows:

- **Introduction:** Covers the document scope, definitions, and references.
- **Project Description:** Introduces the project, its purpose, and the technologies involved.
- **System Overview:** Provides an in-depth look into the system architecture, interfaces, and data management.
- **System Modules:** Details individual system modules, including their structure, dynamic interactions, and diagrams.
- **Bibliography:** Lists references and sources used in the project.

Each section is designed to build upon the previous, ensuring a logical flow of information from conceptualization to implementation. The document aims to be clear and structured, providing both high-level overviews and technical specifics to guide development and implementation.</p>

</details>

### <a name="biblio"></a> 1.4 Bibliography
<details> 

1. Lewis, Patrick, et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. 2020.   
2. LangChain Documentation: [https://python.langchain.com/](https://python.langchain.com/)  
3. FAISS Library: [https://faiss.ai/](https://faiss.ai/)  
4. FastAPI Documentation: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)  
5. PostgreSQL Documentation: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)  
</p>
</details>

## <a name="description"></a> 2 Project Description

### <a name="project-intro"></a> 2.1 Project Introduction

<details> 
<summary>  Describe at an high level what is the goal of the project and a possible solution
    </summary>
    </br>
    <p>The project of RAG divided into 3 sub application:</p>
    <ul>
    <li><b>Reviewer Assistant:</b> This component is designed to review contributions to the portal and provide constructive feedback to ensure consistency and adherence to guidelines. The Reviewer Assistant analyzes inputs such as Markdown documents and OpenAPI Specification (OAS) files, comparing them against pre-defined standards. It offers actionable suggestions for improving content quality and identifies inconsistencies or errors in the submissions.</li>
    <li><b>Writer Assistant:</b> This component supports developers in creating content for the portal. It helps generate tutorials aligned with the portal's guidelines and existing documentation. The Writer Assistant can produce tutorials based on input provided by developers, as well as directly from OpenAPI specifications, ensuring that all generated content is relevant and accurate.</li>
    <li><b>App Developer Assistant:</b> This component assists app developers in building applications that utilize the capabilities documented in the portal. It can generate code libraries based on API specifications and provided examples, streamlining the development process. Additionally, it offers context-specific responses to queries, enabling developers to better understand and implement the portal's functionalities in their applications.</li>
    </ul>
</details>

### <a name="tech"></a> 2.2 Technologies used

<details>  
    <summary> Description of the overall architecture. </summary>  
    
| Name          | Description |
| ------------- | ------------- |
| GitHub        | GitHub is an online platform where developers can store, share, and collaborate on code. It helps teams manage projects, track changes, and work together on software development. |
| Python        | Python is a flexible and easy-to-read programming language with many useful libraries, making it great for tasks like web development and more. |
| HTML          | HTML is the basic language used to create web pages. It structures content using elements like headings, paragraphs, links, and images, helping browsers display websites properly. |
| CSS           | CSS is a style language used to design web pages. It controls colors, fonts, layouts, and spacing, making websites look visually appealing and responsive on different devices. |
| LangChain     | LangChain is a framework for building applications powered by LLMs. It provides tools for chaining different components like prompt engineering, retrieval mechanisms, and memory management. |
| OpenAI API    | OpenAI API provides access to powerful language models like GPT, enabling text generation, summarization, and conversational AI capabilities. |
| FAISS         | FAISS (Facebook AI Similarity Search) is a library for efficient similarity search and dense vector storage, commonly used in RAG to retrieve relevant documents from large datasets. |
| Pinecone      | Pinecone is a vector database optimized for fast and scalable similarity searches, helping improve retrieval efficiency in RAG-based applications. |
| Hugging Face  | Hugging Face provides pre-trained models and APIs for natural language processing (NLP), including transformers for tasks like text generation and embeddings. |
| FastAPI       | FastAPI is a modern web framework for building APIs with Python. It is highly efficient and commonly used to serve LLM-powered applications. |
| Elasticsearch | Elasticsearch is a distributed search engine used for indexing and retrieving documents efficiently, often integrated into RAG architectures. |
| PostgreSQL    | PostgreSQL is a powerful relational database system used for storing structured data and metadata in AI applications. |
| Docker        | Docker helps in containerizing applications, making deployment consistent across different environments. |

</details>  

### <a name="constraints"></a> 2.3 Assumption and Constraint

<details> 
    <summary>Assumptions and constraints of the project implementation
    </summary>
    <b>Assumptions:</b>
    <ul>
        <li>Developers have access to pre-existing documentation that adheres to the given guidelines.
</li>
        <li>The OpenAPI specifications and other relevant input documents are correctly formatted.
</li>
        <li>The AI assistant operates within the Internal Development Portal, which provides a stable environment for integration.
</li>
    </ul>

<b>Constraints:</b>

<ul>
<li>
The assistant's recommendations and generated content must align with pre-existing documentation and portal guidelines.
</li>
</ul>

</details>

## <a name="system-overview"></a> 3 System Overview

<details>
    <summary>
        This section provides a high-level overview of the Developer AI Assistant. It outlines the system's purpose, which is to enhance the Internal Development Portal by providing intelligent assistance to different user roles. The system is designed using a Retrieval Augmented Generation (RAG) architecture and aims to improve content quality, content creation efficiency, and application development support.
    </summary>
    <p>
        The Developer AI Assistant is designed to be integrated into the Internal Development Portal to improve the experience for both content creators and application developers.
        It provides three main components: Reviewer Assistant, Writer Assistant, and App Developer Assistant.
        Leveraging Retrieval Augmented Generation (RAG) architecture, the system aims to understand user queries and provide relevant and context-aware responses by retrieving information from the existing portal content and guidelines.
        The primary goal is to streamline content contribution workflows, ensure content quality and consistency, and empower application developers by providing readily accessible information and code examples.
    </p>
</details>

### <a name="architecture"></a> 3.1 System Architecture

<details>
    <summary>
        This section details the system architecture based on Retrieval Augmented Generation (RAG). It highlights the key components: Retrieval, Augmentation, and Generation, and how they interact within the Developer AI Assistant. The architecture is designed to effectively utilize the knowledge base and provide relevant and context-aware assistance.
    </summary>
    <p>
        The Developer AI Assistant will be built upon a Retrieval Augmented Generation (RAG) architecture.
        This architecture consists of the following key stages:
        <ol>
            <li><b>Retrieval:</b> When a user interacts with the AI Assistant, the system first retrieves relevant information from the knowledge base. This knowledge base comprises:
                <ul>
                    <li>Guidelines on Markdown documentation.</li>
                    <li>Portal and product-specific guidelines.</li>
                    <li>Pre-existing portal documents.</li>
                    <li>OpenAPI specifications (OAS files).</li>
                </ul>
                The retrieval process will involve indexing and searching this knowledge base to find content semantically related to the user's query or input. We will evaluate the use of vector databases for efficient similarity search, and consider complementing it with other database types for structured data and metadata management.
            </li>
            <li><b>Augmentation:</b> The retrieved content is then augmented with the user's original input. This step involves combining the retrieved information with the context of the user's request to provide a richer and more context-aware input for the generation stage.</li>
            <li><b>Generation:</b> Finally, the augmented information is fed into a Generative Model (e.g., a Large Language Model). This model generates the desired output, which could be:
                <ul>
                    <li>Feedback and suggestions for content review.</li>
                    <li>Generated tutorials based on developer input or OpenAPI specs.</li>
                    <li>Code libraries based on API specifications and examples.</li>
                    <li>Answers to user queries based on portal content.</li>
                </ul>
            </li>
        </ol>
        The system will also include a User Interface for users to interact with the AI Assistant.
        Optionally, a multi-agent system may be explored to manage complex workflows and interactions between different components of the AI assistant.
    </p>
</details>

### <a name="interfaces"></a> 3.2 System Interfaces

<details>
    <summary>
        This section describes the system interfaces, focusing on the User Interface for user interaction and the interfaces for data input and output. It emphasizes the importance of a user-friendly interface and clear data flow within the system.
    </summary>
    <p>
        The Developer AI Assistant will provide the following interfaces:
        <ul>
            <li><b>User Interface (UI):</b> A user-friendly interface will be developed to allow users to interact with the AI Assistant. This UI will enable users to:
                <ul>
                    <li>Submit contributions for review.</li>
                    <li>Request tutorial generation.</li>
                    <li>Input OpenAPI specifications.</li>
                    <li>Ask questions related to the portal content and APIs.</li>
                    <li>Receive feedback, suggestions, generated content, and responses.</li>
                </ul>
                The UI will be designed to be intuitive and easy to use for developers with varying levels of technical expertise. Integration with the Internal Development Portal will be a key consideration for the UI design.
            </li>
            <li><b>Data Input Interfaces:</b> The system will ingest data from various sources:
                <ul>
                    <li><b>Markdown Document Guidelines:</b> Programmatic access to guideline documents for content review.</li>
                    <li><b>Portal and Product Specific Guidelines:</b> Programmatic access to these specific guidelines.</li>
                    <li><b>Pre-existing Documents:</b> Access to the existing corpus of documents within the Internal Development Portal. This will likely involve database connections or API access to the portal's content repository.</li>
                    <li><b>User Contributions:</b> Interfaces to receive user-submitted content (Markdown documents, OpenAPI specs, tutorial requests, queries) through the UI.</li>
                    <li><b>OpenAPI Specifications (OAS):</b> Interfaces to ingest OAS files, either through file upload or direct API integration if applicable.</li>
                </ul>
            </li>
            <li><b>Data Output Interfaces:</b> The system will provide outputs through:
                <ul>
                    <li><b>User Interface:</b> Displaying feedback, suggestions, generated tutorials, code libraries, and responses to queries within the UI.</li>
                    <li><b>Internal Development Portal Integration:</b> Interfaces to potentially integrate the AI Assistant's outputs back into the portal, such as saving reviewed documents or publishing generated tutorials (depending on workflow requirements).</li>
                    <li><b>API (Optional):</b> Depending on future needs, an API could be exposed to allow other systems or services to interact with the AI Assistant programmatically.</li>
                </ul>
            </li>
        </ul>
    </p>
</details>

### <a name="data"></a> 3.3 System Data

<details>
    <summary>
        This section outlines the data managed by the system, categorizing it into system inputs and outputs. It details the types of data the system will process and generate, emphasizing the flow of information within the Developer AI Assistant.
    </summary>
    <p>
        The Developer AI Assistant manages various types of data as inputs and outputs during its operation.
    </p>
</details>

#### <a name="inputs"></a> 3.3.1 System Inputs

<details>
    <summary>
        This section details the various inputs to the Developer AI Assistant. These inputs are crucial for the system to perform its functions, including reviewing content, generating tutorials, and assisting app developers. The inputs range from guideline documents to user-provided specifications and queries.
    </summary>
    <p>
        The Developer AI Assistant will process the following inputs:
        <ul>
            <li><b>Guidelines on how to produce Markdown documentations:</b> These are documents outlining the rules and best practices for writing Markdown documentation within the portal. They serve as the standard against which contributions are reviewed.</li>
            <li><b>Additional guidelines specific to the portal and product:</b> These guidelines provide context and rules specific to the Internal Development Portal and the products it documents. They supplement the general Markdown guidelines for content review and generation.</li>
            <li><b>Pre-existing documents assumed to be correctly written:</b> This corpus of existing documents within the portal serves as a reference knowledge base for the AI Assistant. These documents are used for RAG to provide contextually relevant responses and generate content aligned with existing portal standards.</li>
            <li><b>User Contributions (Draft Documents):</b> These are the Markdown documents submitted by developers for review. They are the primary input for the Reviewer Assistant component.</li>
            <li><b>OpenAPI Specifications (OAS files):</b> OAS files serve as input for both the Writer Assistant (to generate tutorials) and the App Developer Assistant (to generate code libraries and provide API information).</li>
            <li><b>Developer Inputs for Tutorial Generation:</b> Developers will provide input, likely in the form of text prompts or outlines, to guide the Writer Assistant in generating tutorials.</li>
            <li><b>App Developer Queries:</b> App developers will input questions or requests related to portal content, API usage, and code examples to the App Developer Assistant.</li>
        </ul>
    </p>
</details>

#### <a name="outputs"></a> 3.3.2 System Ouputs

<details>
    <summary>
        This section details the outputs generated by the Developer AI Assistant. These outputs are the results of the system's functionalities, designed to assist reviewers, content writers, and application developers. The outputs include feedback, generated content, and responses to queries, all aimed at improving the portal and the development process.
    </summary>
    <p>
        The Developer AI Assistant will generate the following outputs:
        <ul>
            <li><b>Review Feedback and Improvement Suggestions:</b> The Reviewer Assistant will provide feedback on draft documents, highlighting areas for improvement and suggesting specific changes to align with guidelines. This output is targeted at content contributors.</li>
            <li><b>Generated Tutorials (based on developer input or OAS):</b> The Writer Assistant will generate tutorials in Markdown format, based on either developer-provided outlines or OpenAPI specifications. These tutorials will be ready for publication on the portal, subject to review.</li>
            <li><b>Generated Code Libraries and Examples:</b> The App Developer Assistant will generate code snippets and libraries in various programming languages, based on API specifications and examples from the portal. This output aims to accelerate application development.</li>
            <li><b>Responses to User Queries:</b> The App Developer Assistant will provide informative responses to app developers' questions, drawing upon the content of the Internal Development Portal. These responses aim to facilitate content navigation and understanding of portal resources.</li>
            <li><b>Documentation (Deliverable):</b> Documentation detailing the design, technology choices, functionality, and usage of the AI assistant will be produced as a key deliverable of the project.</li>
            <li><b>Test Plans, Test Cases, and Test Results (Deliverable):</b> These documents, demonstrating the functionality and performance of the AI assistant, will be produced as part of the project deliverables.</li>
        </ul>
    </p>
</details>

## <a name="sys-module-1"></a> 4 Web Application

### <a name="sd"></a> 4.1 Structural Diagrams

#### <a name="cd"></a> 4.1.1 Class diagram

<details> 
    <summary>The class diagram illustrates the static structure of our system by showing the system's classes, their attributes, methods, and the relationships among the classes.
    </summary>
    <img src="./imgs/Class Diagram.jpg"/>
</details>

#### <a name="od"></a> 4.1.2 Object diagram

<details> 
     <summary>The object diagram provides a snapshot of the system at a particular moment in time, illustrating the instances of classes and their relationships. It helps in understanding the real-world scenarios and interactions between objects within the system. This section will describe the specific objects involved, their attributes, and the links between them, offering a detailed view of the system's state during execution.
    </summary>
     <img src="./imgs/Object Diagram.jpg"/>
</details>

#### <a name="dm"></a> 4.2 Dynamic Models

<details> 
    <summary>
        A Dynamic Diagram in a web application visually represents system interactions, workflows, and real-time data updates. It includes user actions, backend processing, and database interactions.
    </summary>
    <img src="./imgs/Dynamic Diagram.jpg"/>
</details>
