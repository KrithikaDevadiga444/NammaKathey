package com.nammakathey

import android.content.Intent
import android.media.MediaPlayer
import android.net.Uri
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.RecyclerView
import androidx.viewpager2.widget.ViewPager2
import com.nammakathey.data.DataProvider
import com.nammakathey.databinding.ActivityStoryViewerBinding
import com.nammakathey.model.Hero
import com.nammakathey.model.StoryPage
import java.util.*

class StoryViewerActivity : AppCompatActivity(), TextToSpeech.OnInitListener {

    private lateinit var binding: ActivityStoryViewerBinding
    private var hero: Hero? = null
    private var tts: TextToSpeech? = null
    private lateinit var adapter: StoryAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityStoryViewerBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val districtId = intent.getStringExtra("DISTRICT_ID") ?: return
        val heroId = intent.getStringExtra("HERO_ID") ?: return
        hero = DataProvider.getHeroById(districtId, heroId)

        tts = TextToSpeech(this, this)

        setupStoryPager()

        val bounceAnim =
            android.view.animation.AnimationUtils.loadAnimation(this, R.anim.bounce)

        binding.btnToggleLang.setOnClickListener {
            it.startAnimation(bounceAnim)
            DataProvider.isKannada = !DataProvider.isKannada
            adapter.notifyDataSetChanged()
            updateLanguageButtonText()
        }

        binding.btnBack.setOnClickListener {
            it.startAnimation(bounceAnim)
            it.postDelayed({ finish() }, 150)
        }

        binding.btnTTS.setOnClickListener {
            it.startAnimation(bounceAnim)
            readCurrentPage()
        }

        // ✅ DID YOU KNOW BUTTON
        binding.btnDidYouKnow.setOnClickListener {
            it.startAnimation(bounceAnim)
            showDidYouKnowPopup()
        }

        binding.btnTakeQuiz.setOnClickListener {
            it.startAnimation(bounceAnim)
            val intent = Intent(this, QuizActivity::class.java)
            intent.putExtra("DISTRICT_ID", districtId)
            intent.putExtra("HERO_ID", heroId)
            startActivity(intent)
        }

        binding.btnStatue.setOnClickListener {
            it.startAnimation(bounceAnim)
            val gmmIntentUri = Uri.parse(hero?.statueLocation)
            val mapIntent = Intent(Intent.ACTION_VIEW, gmmIntentUri)
            startActivity(mapIntent)
        }

        binding.btnNext.setOnClickListener {
            it.startAnimation(bounceAnim)
            val currentItem = binding.viewPagerStory.currentItem
            if (currentItem < (hero?.storyPages?.size ?: 0) - 1) {
                binding.viewPagerStory.currentItem = currentItem + 1
            }
        }

        binding.btnPrev.setOnClickListener {
            it.startAnimation(bounceAnim)
            val currentItem = binding.viewPagerStory.currentItem
            if (currentItem > 0) {
                binding.viewPagerStory.currentItem = currentItem - 1
            }
        }

        updateLanguageButtonText()
        updatePageIndicator(0)
    }

    private fun setupStoryPager() {
        val pages = hero?.storyPages ?: emptyList()
        adapter = StoryAdapter(pages)
        binding.viewPagerStory.adapter = adapter

        binding.viewPagerStory.registerOnPageChangeCallback(
            object : ViewPager2.OnPageChangeCallback() {
                override fun onPageSelected(position: Int) {
                    updatePageIndicator(position)
                }
            })
    }

    private fun updatePageIndicator(position: Int) {
        val total = hero?.storyPages?.size ?: 0
        binding.tvPageIndicator.text = "${position + 1} / $total"
    }

    private fun updateLanguageButtonText() {
        binding.btnToggleLang.text = if (DataProvider.isKannada) "KN" else "EN"
    }

    private fun readCurrentPage() {
        val currentItem = binding.viewPagerStory.currentItem
        val page = hero?.storyPages?.get(currentItem) ?: return
        val text = if (DataProvider.isKannada) page.textKn else page.textEn

        tts?.language =
            if (DataProvider.isKannada) Locale("kn", "IN") else Locale.US

        val cleanText = text.replace(".", ". ")

        val params = Bundle()
        params.putFloat(TextToSpeech.Engine.KEY_PARAM_VOLUME, 1.0f) // Max volume perception

        tts?.speak(cleanText, TextToSpeech.QUEUE_FLUSH, params, "story_voice")
    }

    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) {
            tts?.language = Locale.US
            tts?.setSpeechRate(1.1f) // Slightly increased for clarity
            tts?.setPitch(1.05f)
            
            // Set AudioAttributes to improve speech clarity and loudness
            val audioAttributes = android.media.AudioAttributes.Builder()
                .setUsage(android.media.AudioAttributes.USAGE_ASSISTANCE_ACCESSIBILITY)
                .setContentType(android.media.AudioAttributes.CONTENT_TYPE_SPEECH)
                .build()
            tts?.setAudioAttributes(audioAttributes)
        }
    }

    // ✅ FINAL FIXED POPUP
    private fun showDidYouKnowPopup() {

        val facts = hero?.didYouKnow ?: return
        if (facts.isEmpty()) return

        val randomFact = facts.random()

        val dialogView = layoutInflater.inflate(R.layout.dialog_did_you_know, null)

        val tvFact = dialogView.findViewById<TextView>(R.id.tvFact)
        val btnClose = dialogView.findViewById<Button>(R.id.btnClose)
        val imgMascot = dialogView.findViewById<ImageView>(R.id.bgMascot)
        val cardPopup = dialogView.findViewById<View>(R.id.cardPopup)

        // ✅ FIXED TEXT (IMPORTANT)
        val factText = if (DataProvider.isKannada)
            randomFact.kn
        else
            randomFact.en

        tvFact.text = factText

        val dialog = android.app.AlertDialog.Builder(this)
            .setView(dialogView)
            .setCancelable(false)
            .create()

        dialog.show()

        dialog.window?.setLayout(
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.MATCH_PARENT
        )
        dialog.window?.setBackgroundDrawableResource(android.R.color.transparent)
        dialog.show()

        // 🎬 animation
        imgMascot.startAnimation(
            android.view.animation.AnimationUtils.loadAnimation(this, R.anim.bounce)
        )
        
        // Scale in animation for popup
        val scaleIn = android.view.animation.ScaleAnimation(
            0.8f, 1.0f, 0.8f, 1.0f,
            android.view.animation.Animation.RELATIVE_TO_SELF, 0.5f,
            android.view.animation.Animation.RELATIVE_TO_SELF, 0.5f
        ).apply {
            duration = 300
            interpolator = android.view.animation.OvershootInterpolator()
        }
        cardPopup?.startAnimation(scaleIn)

        // 🔊 safe media player
        val mediaPlayer = MediaPlayer.create(this, R.raw.pop)
        mediaPlayer?.let {
            it.setOnCompletionListener { mp ->
                mp.release()
            }
            it.start()
        }

        btnClose.setOnClickListener {
            btnClose.startAnimation(android.view.animation.AnimationUtils.loadAnimation(this, R.anim.bounce))
            it.postDelayed({ dialog.dismiss() }, 150)
        }
    }

    override fun onDestroy() {
        tts?.stop()
        tts?.shutdown()
        super.onDestroy()
    }

    class StoryAdapter(private val pages: List<StoryPage>) :
        RecyclerView.Adapter<StoryAdapter.ViewHolder>() {

        class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
            val tvTitle: TextView = view.findViewById(R.id.tvStoryTitle)
            val ivImage: ImageView = view.findViewById(R.id.ivStoryImage)
            val tvText: TextView = view.findViewById(R.id.tvStoryText)
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(R.layout.item_story_page, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val page = pages[position]
            val context = holder.itemView.context

            holder.tvTitle.text =
                if (DataProvider.isKannada) page.titleKn else page.titleEn

            holder.tvText.text =
                if (DataProvider.isKannada) page.textKn else page.textEn

            val resId = context.resources.getIdentifier(
                page.image,
                "drawable",
                context.packageName
            )

            holder.ivImage.setImageResource(
                if (resId != 0) resId else R.drawable.ic_placeholder_hero
            )
        }

        override fun getItemCount() = pages.size
    }
}