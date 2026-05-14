package com.nammakathey

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.nammakathey.data.DataProvider
import com.nammakathey.databinding.ActivityHeroListBinding
import com.nammakathey.model.Hero

class HeroListActivity : AppCompatActivity() {

    private lateinit var binding: ActivityHeroListBinding
    private lateinit var districtId: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityHeroListBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // ✅ Get district ID
        districtId = intent.getStringExtra("DISTRICT_ID") ?: return
        val district = DataProvider.getDistrictById(districtId)

        // ✅ Set title
        binding.tvDistrictTitle.text = "Heroes of ${district?.name}"

        // ✅ Back button
        binding.btnBack.setOnClickListener {
            finish()
        }

        // 🔥 SET BACKGROUND IMAGE (FINAL FIX)
        val imageName = intent.getStringExtra("districtImage")

        imageName?.let {
            val resId = resources.getIdentifier(it, "drawable", packageName)
            if (resId != 0) {
                binding.bgImage.setImageResource(resId)
            }
        }

        // ✅ RecyclerView
        binding.rvHeroes.layoutManager = LinearLayoutManager(this)
        binding.rvHeroes.adapter = HeroAdapter(district?.heroes ?: emptyList()) { hero ->
            val intent = Intent(this, StoryViewerActivity::class.java)
            intent.putExtra("DISTRICT_ID", districtId)
            intent.putExtra("HERO_ID", hero.id)
            startActivity(intent)
        }
    }

    // ✅ Adapter
    class HeroAdapter(
        private val heroes: List<Hero>,
        private val onClick: (Hero) -> Unit
    ) : RecyclerView.Adapter<HeroAdapter.ViewHolder>() {

        class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
            val tvName: TextView = view.findViewById(R.id.tvHeroName)
            val tvDesc: TextView = view.findViewById(R.id.tvHeroDesc)
            val ivImage: ImageView = view.findViewById(R.id.ivHeroImage)
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
            val view = LayoutInflater.from(parent.context)
                .inflate(R.layout.item_hero, parent, false)
            return ViewHolder(view)
        }

        override fun onBindViewHolder(holder: ViewHolder, position: Int) {
            val hero = heroes[position]

            holder.tvName.text = hero.name
            holder.tvDesc.text = hero.shortDesc

            val context = holder.itemView.context
            val resId = context.resources.getIdentifier(
                hero.image,
                "drawable",
                context.packageName
            )

            if (resId != 0) {
                holder.ivImage.setImageResource(resId)
            } else {
                holder.ivImage.setImageResource(R.drawable.ic_placeholder_hero)
            }

            holder.itemView.setOnClickListener {
                onClick(hero)
            }
        }

        override fun getItemCount() = heroes.size
    }
}