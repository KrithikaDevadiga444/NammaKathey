package com.nammakathey

import android.os.Bundle
import android.widget.TextView
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.nammakathey.data.DataProvider
import com.nammakathey.data.UserManager
import com.nammakathey.databinding.ActivityQuizBinding
import com.nammakathey.model.Hero
import android.view.ViewGroup

class QuizActivity : AppCompatActivity() {

    private lateinit var binding: ActivityQuizBinding
    private var hero: Hero? = null
    private var currentQuestionIndex = 0
    private var score = 0
    private var isAnswered = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityQuizBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val districtId = intent.getStringExtra("DISTRICT_ID") ?: return
        val heroId = intent.getStringExtra("HERO_ID") ?: return
        hero = DataProvider.getHeroById(districtId, heroId)

        loadQuestion()

        binding.btnBack.setOnClickListener { finish() }

        val bounceAnim =
            android.view.animation.AnimationUtils.loadAnimation(this, R.anim.bounce)

        binding.btnNext.setOnClickListener {
            it.startAnimation(bounceAnim)

            currentQuestionIndex++

            if (currentQuestionIndex < (hero?.quiz?.size ?: 0)) {
                loadQuestion()
            } else {
                showResult()
            }
        }

        val optionButtons = listOf(
            binding.btnOption1,
            binding.btnOption2,
            binding.btnOption3,
            binding.btnOption4
        )

        optionButtons.forEachIndexed { index, button ->
            button.setOnClickListener {
                it.startAnimation(bounceAnim)

                if (!isAnswered) {
                    checkAnswer(index, button)
                }
            }
        }
    }

    private fun loadQuestion() {

        isAnswered = false
        binding.btnNext.visibility = View.GONE

        val question = hero?.quiz?.get(currentQuestionIndex) ?: return

        binding.tvQuestion.text = question.questionEn

        val options = question.optionsEn

        val optionButtons = listOf(
            binding.btnOption1,
            binding.btnOption2,
            binding.btnOption3,
            binding.btnOption4
        )

        for (i in optionButtons.indices) {

            if (i < options.size) {
                optionButtons[i].visibility = View.VISIBLE
                optionButtons[i].text = options[i]

                // 🔥 VERY IMPORTANT FIX
                optionButtons[i].backgroundTintList = null
                optionButtons[i].setBackgroundResource(R.drawable.bg_option)

                optionButtons[i].setTextColor(
                    ContextCompat.getColor(this, R.color.text_primary)
                )

            } else {
                optionButtons[i].visibility = View.GONE
            }
        }
    }

    private fun checkAnswer(selectedIndex: Int, selectedButton: Button) {

        isAnswered = true

        val question = hero?.quiz?.get(currentQuestionIndex) ?: return

        val optionButtons = listOf(
            binding.btnOption1,
            binding.btnOption2,
            binding.btnOption3,
            binding.btnOption4
        )

        val correctIndex = question.correctAnswerIndex
        val correctButton = optionButtons[correctIndex]

        if (selectedIndex == correctIndex) {

            score++

            // ✅ REMOVE TINT + APPLY GREEN
            selectedButton.backgroundTintList = null
            selectedButton.setBackgroundResource(R.drawable.bg_correct)

            selectedButton.setTextColor(
                ContextCompat.getColor(this, android.R.color.white)
            )

        } else {

            // ❌ WRONG (RED)
            selectedButton.backgroundTintList = null
            selectedButton.setBackgroundResource(R.drawable.bg_wrong)

            selectedButton.setTextColor(
                ContextCompat.getColor(this, android.R.color.white)
            )

            // ✅ CORRECT (GREEN)
            correctButton.backgroundTintList = null
            correctButton.setBackgroundResource(R.drawable.bg_correct)

            correctButton.setTextColor(
                ContextCompat.getColor(this, android.R.color.white)
            )
        }

        // 🚫 DO NOT DISABLE (causes grey override in some themes)
        // optionButtons.forEach { it.isEnabled = false }

        binding.btnNext.visibility = View.VISIBLE
    }

    private fun showResult() {

        val total = hero?.quiz?.size ?: 0

        if (score == total && total > 0) {

            saveBadge()

            Toast.makeText(
                this,
                "Awesome! You earned a Hero Badge!",
                Toast.LENGTH_LONG
            ).show()

            try {
                val notification =
                    android.media.RingtoneManager.getDefaultUri(
                        android.media.RingtoneManager.TYPE_NOTIFICATION
                    )
                val r = android.media.RingtoneManager.getRingtone(
                    applicationContext,
                    notification
                )
                r.play()
            } catch (e: Exception) {
                e.printStackTrace()
            }

            val glowAnim =
                android.view.animation.AnimationUtils.loadAnimation(this, R.anim.glow)

            binding.tvQuestion.text = "Badge Earned!"
            binding.tvQuestion.startAnimation(glowAnim)

            binding.llOptions.visibility = View.GONE
            binding.btnNext.visibility = View.GONE

            binding.root.postDelayed({
                showResultDialog()
            }, 2000)

        } else {
            showResultDialog()
        }
    }

    private fun showResultDialog() {

        val dialogView = layoutInflater.inflate(R.layout.dialog_quiz_result, null)

        val tvScore = dialogView.findViewById<TextView>(R.id.tvScore)
        val tvMessage = dialogView.findViewById<TextView>(R.id.tvMessage)
        val btnOk = dialogView.findViewById<Button>(R.id.btnOk)

        val total = hero?.quiz?.size ?: 0

        tvScore.text = "$score / $total"

        tvMessage.text = when {
            score == total -> "Perfect! 🎉"
            score >= total / 2 -> "Good Job 👍"
            else -> "Try Again 💪"
        }

        val dialog = AlertDialog.Builder(this)
            .setView(dialogView)
            .setCancelable(false)
            .create()

        btnOk.setOnClickListener {
            dialog.dismiss()
            finish()
        }

        dialog.show()

        // 🔥 THIS LINE FIXES FULL SCREEN BACKGROUND
        dialog.window?.setLayout(
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.MATCH_PARENT
        )
    }

    private fun saveBadge() {
        hero?.let {
            UserManager.addBadgeToCurrentUser(this, it.id)
        }
    }
}