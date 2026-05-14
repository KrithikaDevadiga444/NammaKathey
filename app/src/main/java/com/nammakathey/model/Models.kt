package com.nammakathey.model

import com.google.gson.annotations.SerializedName

data class AppData(
    val districts: List<District>
)

data class DidYouKnow(
    val en: String,
    val kn: String
)

data class District(
    val id: String,
    val name: String,
    val image: String,
    val heroes: List<Hero>
)

data class Hero(
    val id: String,
    val name: String,
    val image: String,
    val shortDesc: String,
    val storyPages: List<StoryPage>,
    val quiz: List<QuizQuestion>,
    val statueLocation: String,
    val didYouKnow: List<DidYouKnow> = emptyList()
)

data class StoryPage(
    val titleEn: String,
    val titleKn: String,
    val image: String,
    val textEn: String,
    val textKn: String
)

data class QuizQuestion(
    val questionEn: String,
    val optionsEn: List<String>,
    val correctAnswerIndex: Int
)
