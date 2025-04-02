
### User Requirements Specification Document
##### DIBRIS – Università di Genova. Scuola Politecnica, Software Engineering Course 80154


**VERSION : 1.1**

**Authors**  
- SOBHAN BAZOUBANDI

- AMIRMAHDI ABOUTALEBI

- AMIRHOSSEIN YAGHOUBNEZHAD

**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
| 1.0 | 13/05/2024 | SOBHAN BAZOUBANDI, AMIRMAHDI ABOUTALEBI, AMIRHOSSEIN YAGHOUBNEZHAD |  |
| 1.1 | 10/06/2024 | SOBHAN BAZOUBANDI, AMIRMAHDI ABOUTALEBI, AMIRHOSSEIN YAGHOUBNEZHAD |  |

# Table of Contents

1. [Introduction](#p1)
	1. [Document Scope](#sp1.1)
	2. [Definitios and Acronym](#sp1.2) 
	3. [References](#sp1.3)
2. [System Description](#p2)
	1. [Context and Motivation](#sp2.1)
	2. [Project Objectives](#sp2.2)
3. [Requirement](#p3)
 	1. [Stakeholders](#sp3.1)
 	2. [Functional Requirements](#sp3.2)
 	3. [Non-Functional Requirements](#sp3.3)
  
  

<a name="p1"></a>

## 1. Introduction
<a name="sp1.1"></a>

### 1.1 Document Scope
This document outlines the user requirements for the RAG Implementation for LLM Study Platform project at Ericsson. The AI Assistant will include functionalities for reviewing, writing, and supporting development tasks. It will be integrated into the Internal Development Portal and provide a user-friendly interface for interacting with the system.

<a name="sp1.2"></a>

### 1.2 Definitios and Acronym


| Acronym				| Definition | 
| ------------------------------------- | ----------- | 
| LLM                                   | Large Language Model |
| RAG                                   | Retriever-Augmented-Generator |
| LLaMA                                 | Family of autoregressive large language models released by Meta AI |
| NLP					| Natural Language Processing |
| FT					| Fine Tuning |
| RNN					| Recurrent Neural Networks |
| GAI					| Generative Artificial Intelligence
| AI					| Artificial Intelligence
| OAS					| OpenAPI Specification
| UI					| User Interface


<a name="sp1.3"></a>

### 1.3 References 
Knowledge Graph for RAG: (DeepLearning ai) : <a href = "https://learn.deeplearning.ai/courses/knowledge-graphs-rag/">Course Link</a>
Large Language Model Pathway : <a href = "https://datasciencedojo.com/blog/large-language-models-pathway/">Article Link</a>
RAG Method : <a href = "https://paperswithcode.com/method/rag">Paper Link</a>
Additional :
https://www.datacamp.com/blog/what-is-retrieval-augmented-generation-rag

https://www.nvidia.com/en-us/glossary/generative-ai/

https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/

https://www.linkedin.com/pulse/rag-architecture-deep-dive-frank-denneman-4lple/

https://www.youtube.com/watch?v=aywZrzNaKjs

https://www.youtube.com/watch?v=CPgp8MhmGVY

https://medium.aiplanet.com/implementing-rag-using-langchain-ollama-and-chainlit-on-windows-using-wsl-92d14472f15d

https://www.youtube.com/watch?v=rIRkxZSn-A87

https://python.langchain.com/docs/get_started/introduction

https://www.youtube.com/watch?v=ZD3vP6F2At4&pp=ygUbbGFuZ2NoYWluIGFnZW50cyByZWZsZWN0aW9u

https://www.youtube.com/watch?v=pbAd8O1Lvm4&pp=ygUbbGFuZ2NoYWluIGFnZW50cyByZWZsZWN0aW9uCheers
<a name="p2"></a>

## 2. System Description
<a name="sp2.15"></a>

### 2.1 Context and Motivation
The project aims to harness the capabilities of Large Language Models (LLMs), particularly through the implementation of Retriever-Augmented-Generator (RAG) pipelines, to enhance the study platform at Ericsson. By integrating these advanced AI technologies, the project seeks to improve the efficiency, accuracy, and user experience of the platform. The motivation behind this initiative is to leverage the state-of-the-art capabilities of LLMs to provide better support and resources to users, thereby facilitating more effective learning and project management.

<a name="sp2.2"></a>

### 2.2 Project Obectives 
The objective of this project is to develop an AI Assistant based on RAG (Retrieval
Augmented Generation) architecture for our Internal Development Portal, a platform used
by developers for cloud-native product development. The AI assistant should support both
the internal platform developers, during the writing of guidelines, tutorials and API specs,
and the app developer with the content navigation and by generating code libraries or
examples.

<a name="p3"></a>

## 3. Requirements

| Priorità | Significato | 
| --------------- | ----------- | 
| M | **Mandatory:**   |
| D | **Desiderable:** |
| O | **Optional:**    |
| E | **future Enhancement:** |

<a name="sp3.1"></a>
### 3.1 Stakeholders
Internal stakeholders: Ericsson platform developers, project managers, and the internal development team.
External stakeholders: App developers and the users of the internal development portal.
<a name="sp3.2"></a>
### 3.2 Functional Requirements 

| ID | Description | Priority |
| --- | ----------- | -------- |
| 1.0 | The system should take as input a guidlines on how to produce markdown documentations. | M |
| 2.0 | The system should take as input additional guidelines specific to the portal and product | M |
| 3.0 | The system should take as input pre-existing documents assumed to be correctly written | M 
| 4.0 | The system should have three assistant : Writer, Reviewer, App Developer | M
| 5.0 | The Review Assistant should review the contributions made to the portal | M 
| 6.0 | The Review Assistant should analyze the input that against the provided guidelines | M 
| 7.0 | The Review Assistant should give feedback and improvement suggestion on draft | M
| 8.0 | The Writer Assistant should generate tutorials based on the input given by the developers aligned with the guideline and the existing content | M 
| 9.0 | The Writer Assistant should generate tutorials using OpenAPI spec | M 
| 10.0 | The Writer Assistant should take OpenAPI spec as input | M 
| 11.0 | The App Developer Assistant should generate code libraries based on API specifications and examples | M
<a name="sp3.3"></a>
### 3.2 Non-Functional Requirements 

| ID | Description | Priority |
| --- | ----------- | -------- | 
| 1.0 | The AI assistant should provide a user-friendly interface. | M |
| 2.0 | Handle the knowledge base effectively, possibly evaluating the use of a vector database. | M |
| 3.0 | The system should ensure data privacy and security. | M |
