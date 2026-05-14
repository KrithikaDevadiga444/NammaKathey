package com.nammakathey

import android.content.Intent
import android.os.Bundle
import android.view.animation.AnimationUtils
import android.widget.ImageView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.nammakathey.data.UserManager
import com.nammakathey.databinding.ActivityLoginBinding

class LoginActivity : AppCompatActivity() {

    private lateinit var binding: ActivityLoginBinding

    // ✅ default avatar
    private var selectedAvatarResId: Int = R.drawable.avatar_boy

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val bounceAnim = AnimationUtils.loadAnimation(this, R.anim.bounce)

        // ✅ SET DIFFERENT IMAGES
        binding.ivAvatar1.setImageResource(R.drawable.avatar_boy)
        binding.ivAvatar2.setImageResource(R.drawable.avatar_girl)
        binding.ivAvatar3.setImageResource(R.drawable.avatar_hero)

        // ✅ CLICK EVENTS
        binding.ivAvatar1.setOnClickListener {
            it.startAnimation(bounceAnim)
            selectAvatar(binding.ivAvatar1, R.drawable.avatar_boy)
        }

        binding.ivAvatar2.setOnClickListener {
            it.startAnimation(bounceAnim)
            selectAvatar(binding.ivAvatar2, R.drawable.avatar_girl)
        }

        binding.ivAvatar3.setOnClickListener {
            it.startAnimation(bounceAnim)
            selectAvatar(binding.ivAvatar3, R.drawable.avatar_hero)
        }

        binding.btnStart.setOnClickListener {
            it.startAnimation(bounceAnim)

            val name = binding.etName.text.toString().trim()
            if (name.isEmpty()) {
                binding.tilName.error = "Please enter your name"
                return@setOnClickListener
            }

            UserManager.addUser(this, name, selectedAvatarResId)

            Toast.makeText(this, "Welcome, $name to Namma-Kathey!", Toast.LENGTH_SHORT).show()

            val intent = Intent(this, MainActivity::class.java)
            intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
            startActivity(intent)
            finish()
        }
    }

    private fun selectAvatar(selectedView: ImageView, resId: Int) {
        selectedAvatarResId = resId

        // Reset all
        binding.ivAvatar1.setBackgroundColor(
            ContextCompat.getColor(this, android.R.color.transparent)
        )
        binding.ivAvatar2.setBackgroundColor(
            ContextCompat.getColor(this, android.R.color.transparent)
        )
        binding.ivAvatar3.setBackgroundColor(
            ContextCompat.getColor(this, android.R.color.transparent)
        )

        // Highlight selected
        selectedView.setBackgroundColor(
            ContextCompat.getColor(this, R.color.pastel_yellow)
        )
    }
}